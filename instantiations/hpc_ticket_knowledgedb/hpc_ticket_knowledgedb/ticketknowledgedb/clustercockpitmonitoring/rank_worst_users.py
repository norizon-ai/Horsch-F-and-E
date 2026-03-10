#!/usr/bin/env python3
"""
Rank users by GPU resource waste.

Scoring factors:
- Number of underutilized jobs
- Total GPU-hours wasted
- GPU type weighting (A100/H100/H200 count more than A40)
- Severity of underutilization
"""

import requests
import json
from datetime import datetime, timedelta
from collections import defaultdict
import os
import sys

# Configuration
JWT_TOKEN = os.getenv("CLUSTERCOCKPIT_JWT", "")
if not JWT_TOKEN:
    print("Error: CLUSTERCOCKPIT_JWT environment variable not set")
    print("Export it from config.sh first:")
    print('  source config.sh && export CLUSTERCOCKPIT_JWT="$JWT"')
    sys.exit(1)

API_BASE_URL = "https://monitoring.nhr.fau.de"
CLUSTERS = ["alex", "helma"]

# Filter criteria
MIN_DURATION_HOURS = 4
MAX_GPU_UTILIZATION = 70.0
DAYS_LOOKBACK = 3

# GPU type weights (higher = more valuable resource being wasted)
GPU_TYPE_WEIGHTS = {
    "h200": 2.5,    # H200 - most powerful
    "h100": 2.0,    # H100
    "a100": 1.2,    # A100
    "a40": 1.0,     # A40 - baseline
    "default": 1.5  # Unknown GPU types
}

def get_gpu_weight(subcluster):
    """
    Determine GPU weight based on subcluster name.
    """
    subcluster_lower = subcluster.lower() if subcluster else ""
    
    for gpu_type, weight in GPU_TYPE_WEIGHTS.items():
        if gpu_type in subcluster_lower:
            return weight, gpu_type.upper()
    
    return GPU_TYPE_WEIGHTS["default"], "UNKNOWN"

def calculate_waste_score(job):
    """
    Calculate waste score for a job.
    
    Score = GPU-hours wasted * GPU weight * utilization penalty
    
    GPU-hours wasted = num_gpus * duration_hours * (1 - utilization/100)
    Utilization penalty = higher penalty for extremely low utilization
    """
    duration_hours = job["duration_hours"]
    num_gpus = job["num_gpus"]
    gpu_util = job["gpu_util_percent"]
    gpu_weight = job["gpu_weight"]
    
    # Base waste: GPU-hours that were underutilized
    gpu_hours_wasted = num_gpus * duration_hours * (1 - gpu_util / 100.0)
    
    # Utilization penalty: 0% util gets 2x penalty, 50% util gets 1.2x penalty
    if gpu_util == 0:
        util_penalty = 2.0
    elif gpu_util < 10:
        util_penalty = 1.8
    elif gpu_util < 30:
        util_penalty = 1.5
    elif gpu_util < 50:
        util_penalty = 1.2
    else:
        util_penalty = 1.0
    
    # Final waste score
    waste_score = gpu_hours_wasted * gpu_weight * util_penalty
    
    return waste_score, gpu_hours_wasted

# Calculate time range
end_time = int(datetime.now().timestamp())
start_time = int((datetime.now() - timedelta(days=DAYS_LOOKBACK)).timestamp())
start_date = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d")
end_date = datetime.fromtimestamp(end_time).strftime("%Y-%m-%d")

print(f"🔍 Analyzing GPU resource waste by user")
print(f"📅 Time range: {start_date} to {end_date} ({DAYS_LOOKBACK} days)")
print(f"⏱️  Min duration: {MIN_DURATION_HOURS} hours")
print(f"📊 Max GPU utilization: {MAX_GPU_UTILIZATION}%")
print(f"{'='*70}")
print(f"\n📖 METRIC DEFINITIONS:")
print(f"{'='*70}")
print(f"• Waste Score: Composite metric = GPU-hours wasted × GPU weight × penalty")
print(f"  - Higher score = more valuable resources wasted")
print(f"  - GPU weights: H200 (2.5x), H100 (2.0x), A100 (1.2x), A40 (1.0x)")
print(f"  - Utilization penalty: 0% util=2.0x, <10%=1.8x, <30%=1.5x, <50%=1.2x")
print(f"\n• GPU-hours Wasted: Total GPU time underutilized")
print(f"  - Formula: Σ(GPUs × Hours × (1 - Utilization%))")
print(f"  - Example: 4 GPUs × 10h × (1 - 0.3) = 28 GPU-hours wasted")
print(f"\n• Efficiency Rate: Overall GPU utilization across all jobs")
print(f"  - Formula: (1 - Wasted/Allocated) × 100%")
print(f"  - 100% = Perfect utilization, 0% = Complete waste")
print(f"  - Example: Used 70 of 100 GPU-hours → 70% efficiency")
print(f"\n• Underutilization Rate: Percentage of jobs below {MAX_GPU_UTILIZATION}% GPU usage")
print(f"  - Shows how consistent/inconsistent user's GPU usage is")
print(f"{'='*70}\n")

# User statistics
user_stats = defaultdict(lambda: {
    "jobs": [],
    "total_waste_score": 0.0,
    "total_gpu_hours_wasted": 0.0,
    "total_gpu_hours_allocated": 0.0,
    "num_underutilized_jobs": 0,
    "num_total_gpu_jobs": 0,
    "worst_job": None,
    "gpu_types_used": set(),
    "total_gpus_used": 0
})

total_jobs_checked = 0
total_gpu_jobs = 0
total_excluded_software_jobs = 0

for cluster in CLUSTERS:
    print(f"🖥️  Querying cluster: {cluster}")
    
    url = f"{API_BASE_URL}/userapi/jobs/"
    params = {
        "cluster": cluster,
        "start-time": f"{start_time}-{end_time}",
        "items-per-page": 1000,
        "with-metadata": "true"
    }
    
    headers = {"X-Auth-Token": JWT_TOKEN}
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        jobs = data.get("jobs", [])
        print(f"  ✓ Found {len(jobs)} jobs")
        
        for job in jobs:
            total_jobs_checked += 1
            
            # Extract job details
            job_id = job.get("jobId")
            duration_seconds = job.get("duration", 0)
            duration_hours = duration_seconds / 3600
            num_acc = job.get("numAcc", 0)
            footprint = job.get("footprint")
            user = job.get("user", "unknown")
            partition = job.get("partition", "unknown")
            subcluster = job.get("subCluster", "unknown")
            start_time_unix = job.get("startTime", 0)
            job_state = job.get("jobState", "unknown")
            
            # Check metadata for known simulation software (e.g., GROMACS)
            # These jobs may have low GPU utilization by design
            metadata = job.get("metaData", {})
            skip_job = False
            
            if metadata:
                # Check for GROMACS or other simulation software that's known to have lower GPU util
                metadata_str = json.dumps(metadata).lower()
                excluded_software = ["gromacs", "amber", "namd"]  # Add more as needed
                
                for software in excluded_software:
                    if software in metadata_str:
                        skip_job = True
                        total_excluded_software_jobs += 1
                        break
            
            # Must have GPUs
            if num_acc == 0:
                continue
            
            total_gpu_jobs += 1
            
            # Track all GPU jobs for this user
            gpu_weight, gpu_type = get_gpu_weight(subcluster)
            gpu_hours_allocated = num_acc * duration_hours
            
            user_stats[user]["num_total_gpu_jobs"] += 1
            user_stats[user]["total_gpu_hours_allocated"] += gpu_hours_allocated * gpu_weight
            user_stats[user]["gpu_types_used"].add(gpu_type)
            user_stats[user]["total_gpus_used"] += num_acc
            
            # Skip jobs from excluded software
            if skip_job:
                continue
            
            # Must run longer than minimum duration
            if duration_hours < MIN_DURATION_HOURS:
                continue
            
            # Check GPU utilization
            if footprint is None:
                continue
            
            gpu_util = footprint.get("acc_utilization_avg", None)
            
            if gpu_util is None:
                continue
            
            # GPU utilization below threshold = underutilized
            if gpu_util < MAX_GPU_UTILIZATION:
                start_time_str = datetime.fromtimestamp(start_time_unix).strftime("%Y-%m-%d %H:%M:%S")
                
                job_data = {
                    "cluster": cluster,
                    "job_id": job_id,
                    "partition": partition,
                    "subcluster": subcluster,
                    "gpu_type": gpu_type,
                    "gpu_weight": gpu_weight,
                    "state": job_state,
                    "duration_hours": round(duration_hours, 2),
                    "num_gpus": num_acc,
                    "gpu_util_percent": round(gpu_util, 2),
                    "cpu_load_avg": round(footprint.get("cpu_load_avg", 0), 2),
                    "start_time": start_time_str
                }
                
                waste_score, gpu_hours_wasted = calculate_waste_score(job_data)
                job_data["waste_score"] = round(waste_score, 2)
                job_data["gpu_hours_wasted"] = round(gpu_hours_wasted, 2)
                
                # Update user stats
                user_stats[user]["jobs"].append(job_data)
                user_stats[user]["total_waste_score"] += waste_score
                user_stats[user]["total_gpu_hours_wasted"] += gpu_hours_wasted
                user_stats[user]["num_underutilized_jobs"] += 1
                
                # Track worst single job
                if (user_stats[user]["worst_job"] is None or 
                    waste_score > user_stats[user]["worst_job"]["waste_score"]):
                    user_stats[user]["worst_job"] = job_data
    
    except requests.exceptions.RequestException as e:
        print(f"  ✗ Error querying {cluster}: {e}")
        continue

# Calculate rankings
user_rankings = []
for user, stats in user_stats.items():
    if stats["num_underutilized_jobs"] == 0:
        continue
    
    # Efficiency rate (lower is worse)
    efficiency_rate = 0
    if stats["total_gpu_hours_allocated"] > 0:
        efficiency_rate = (1 - stats["total_gpu_hours_wasted"] / stats["total_gpu_hours_allocated"]) * 100
    
    user_rankings.append({
        "user": user,
        "waste_score": round(stats["total_waste_score"], 2),
        "gpu_hours_wasted": round(stats["total_gpu_hours_wasted"], 2),
        "gpu_hours_allocated": round(stats["total_gpu_hours_allocated"], 2),
        "efficiency_rate": round(efficiency_rate, 2),
        "num_underutilized_jobs": stats["num_underutilized_jobs"],
        "num_total_gpu_jobs": stats["num_total_gpu_jobs"],
        "underutilization_rate": round(stats["num_underutilized_jobs"] / stats["num_total_gpu_jobs"] * 100, 1),
        "gpu_types": sorted(list(stats["gpu_types_used"])),
        "worst_job": stats["worst_job"],
        "all_jobs": stats["jobs"],
        "total_gpus_used": stats["total_gpus_used"]
    })

# Sort by waste score (highest first)
user_rankings.sort(key=lambda x: x["waste_score"], reverse=True)

# Print results
print(f"\n{'='*70}")
print(f"📊 SUMMARY")
print(f"{'='*70}")
print(f"Total jobs checked: {total_jobs_checked}")
print(f"Total GPU jobs: {total_gpu_jobs}")
print(f"Excluded software jobs: {total_excluded_software_jobs} (GROMACS, Amber, NAMD)")
print(f"Total users with underutilized jobs: {len(user_rankings)}")
print(f"{'='*70}\n")

if user_rankings:
    print(f"⚠️  WORST GPU USERS RANKING (by waste score)")
    print(f"{'='*70}\n")
    
    for i, user_data in enumerate(user_rankings, 1):
        print(f"{i}. 👤 User: {user_data['user']}")
        print(f"   💯 Waste Score: {user_data['waste_score']:.1f} points")
        print(f"      └─ Calculation: Σ(GPU-hours wasted × GPU weight × util penalty) across all jobs")
        
        print(f"   ⚡ GPU-Hours: {user_data['gpu_hours_wasted']:.1f} wasted / {user_data['gpu_hours_allocated']:.1f} allocated")
        print(f"      └─ Wasted calculation: Σ(num_gpus × hours × (1 - utilization/100))")
        print(f"      └─ Example from jobs: ", end="")
        # Show calculation for first 2 underutilized jobs as examples
        example_jobs = user_data['all_jobs'][:2]
        examples = []
        for job in example_jobs:
            calc = f"{job['num_gpus']}×{job['duration_hours']:.1f}h×(1-{job['gpu_util_percent']/100:.2f})={job['gpu_hours_wasted']:.1f}"
            examples.append(calc)
        print(" + ".join(examples) + (" + ..." if len(user_data['all_jobs']) > 2 else ""))
        
        efficiency = user_data['efficiency_rate']
        wasted = user_data['gpu_hours_wasted']
        allocated = user_data['gpu_hours_allocated']
        print(f"   📊 Efficiency Rate: {efficiency:.1f}%")
        print(f"      └─ Calculation: (1 - {wasted:.1f}/{allocated:.1f}) × 100 = {efficiency:.1f}%")
        
        print(f"   📋 Jobs: {user_data['num_underutilized_jobs']} underutilized / {user_data['num_total_gpu_jobs']} total GPU jobs ({user_data['underutilization_rate']}%)")
        print(f"      └─ Underutilization rate: ({user_data['num_underutilized_jobs']}/{user_data['num_total_gpu_jobs']}) × 100 = {user_data['underutilization_rate']:.1f}%")
        
        print(f"   🎮 GPU Types: {', '.join(user_data['gpu_types'])}")
        print(f"   📈 Total GPUs: {user_data['total_gpus_used']} GPUs allocated across all jobs")
        
        if user_data["worst_job"]:
            wj = user_data["worst_job"]
            print(f"   🔥 Worst Job: {wj['job_id']} - {wj['num_gpus']}x {wj['gpu_type']} @ {wj['gpu_util_percent']}% util, {wj['duration_hours']}h")
            
            # Show detailed calculation for worst job
            gpu_h_wasted = wj['gpu_hours_wasted']
            waste_score = wj['waste_score']
            gpu_weight = wj['gpu_weight']
            util = wj['gpu_util_percent']
            
            # Determine penalty used
            if util == 0:
                penalty = 2.0
            elif util < 10:
                penalty = 1.8
            elif util < 30:
                penalty = 1.5
            elif util < 50:
                penalty = 1.2
            else:
                penalty = 1.0
            
            print(f"      └─ GPU-h wasted: {wj['num_gpus']} GPUs × {wj['duration_hours']:.1f}h × (1 - {util/100:.2f}) = {gpu_h_wasted:.1f}")
            print(f"      └─ Waste score: {gpu_h_wasted:.1f} GPU-h × {gpu_weight}× weight × {penalty}× penalty = {waste_score:.1f} pts")
        print()
    
    # Save detailed results
    output_file = "worst_users_ranking.json"
    with open(output_file, "w") as f:
        json.dump(user_rankings, f, indent=2, default=str)
    print(f"💾 Detailed results saved to: {output_file}")
    
    # Print top offenders summary
    print(f"\n{'='*70}")
    print(f"🏆 TOP 10 Compute Bandits")
    print(f"📅 Period: {start_date} to {end_date}")
    print(f"{'='*70}")
    for i, user_data in enumerate(user_rankings[:10], 1):
        print(f"{i}. {user_data['user']}: "
              f"{user_data['waste_score']:.0f} pts | "
              f"{user_data['gpu_hours_wasted']:.0f}/{user_data['gpu_hours_allocated']:.0f} GPU-h wasted | "
              f"{user_data['efficiency_rate']:.0f}% eff | "
              f"{user_data['num_underutilized_jobs']}/{user_data['num_total_gpu_jobs']} jobs bad | "
              f"{user_data['total_gpus_used']} GPUs | "
              f"{', '.join(user_data['gpu_types'])}")
    
    # Detailed explanations footer
    print(f"\n{'='*70}")
    print(f"📊 COLUMN EXPLANATIONS:")
    print(f"{'='*70}")
    print(f"• pts = Waste Score (weighted metric, higher = worse)")
    print(f"• GPU-h wasted = GPU-hours underutilized / total allocated")
    print(f"• eff = Efficiency Rate (higher = better GPU usage)")
    print(f"• jobs bad = Underutilized jobs / total GPU jobs")
    print(f"• GPUs = Total number of GPUs allocated across all jobs")
    print(f"• GPU types = Hardware accelerator models used (H200/H100/A100/A40)")
    print(f"{'='*70}")
else:
    print("✅ No users with underutilized GPU jobs found!")
