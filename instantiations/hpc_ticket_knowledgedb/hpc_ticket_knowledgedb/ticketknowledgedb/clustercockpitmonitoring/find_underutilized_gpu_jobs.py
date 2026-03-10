#!/usr/bin/env python3
"""
Find GPU jobs with low accelerator utilization.

Queries ClusterCockpit API for jobs in the last 3 days that:
- Ran for more than 2 hours
- Had GPUs allocated (numAcc > 0)
- GPU utilization below 70%
"""

import requests
import json
from datetime import datetime, timedelta
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
CLUSTERS = ["alex", "helma"]  # Query multiple clusters

# Filter criteria
MIN_DURATION_HOURS = 2
MAX_GPU_UTILIZATION = 70.0
DAYS_LOOKBACK = 3

# Calculate time range
end_time = int(datetime.now().timestamp())
start_time = int((datetime.now() - timedelta(days=DAYS_LOOKBACK)).timestamp())

print(f"🔍 Searching for underutilized GPU jobs")
print(f"📅 Time range: Last {DAYS_LOOKBACK} days")
print(f"⏱️  Min duration: {MIN_DURATION_HOURS} hours")
print(f"📊 Max GPU utilization: {MAX_GPU_UTILIZATION}%")
print(f"{'='*60}\n")

underutilized_jobs = []
total_jobs_checked = 0
total_gpu_jobs = 0

for cluster in CLUSTERS:
    print(f"🖥️  Querying cluster: {cluster}")
    
    # Query API - get all jobs (not just running)
    url = f"{API_BASE_URL}/userapi/jobs/"
    params = {
        "cluster": cluster,
        "start-time": f"{start_time}-{end_time}",
        "items-per-page": 1000  # Adjust as needed
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
            start_time_unix = job.get("startTime", 0)
            job_state = job.get("jobState", "unknown")
            
            # Filter 1: Must have GPUs
            if num_acc == 0:
                continue
            
            total_gpu_jobs += 1
            
            # Filter 2: Must run longer than minimum duration
            if duration_hours < MIN_DURATION_HOURS:
                continue
            
            # Filter 3: Check GPU utilization
            if footprint is None:
                # No metrics available yet (might be too early)
                continue
            
            gpu_util = footprint.get("acc_utilization_avg", None)
            
            if gpu_util is None:
                continue
            
            # Filter 4: GPU utilization below threshold
            if gpu_util < MAX_GPU_UTILIZATION:
                start_time_str = datetime.fromtimestamp(start_time_unix).strftime("%Y-%m-%d %H:%M:%S")
                
                underutilized_jobs.append({
                    "cluster": cluster,
                    "job_id": job_id,
                    "user": user,
                    "partition": partition,
                    "state": job_state,
                    "duration_hours": round(duration_hours, 2),
                    "num_gpus": num_acc,
                    "gpu_util_percent": round(gpu_util, 2),
                    "cpu_load_avg": round(footprint.get("cpu_load_avg", 0), 2),
                    "mem_used_max_gb": round(footprint.get("mem_used_max", 0), 2),
                    "start_time": start_time_str
                })
    
    except requests.exceptions.RequestException as e:
        print(f"  ✗ Error querying {cluster}: {e}")
        continue

# Print results
print(f"\n{'='*60}")
print(f"📊 SUMMARY")
print(f"{'='*60}")
print(f"Total jobs checked: {total_jobs_checked}")
print(f"Jobs with GPUs: {total_gpu_jobs}")
print(f"Underutilized GPU jobs: {len(underutilized_jobs)}")
print(f"{'='*60}\n")

if underutilized_jobs:
    print(f"⚠️  UNDERUTILIZED GPU JOBS (GPU util < {MAX_GPU_UTILIZATION}%)")
    print(f"{'='*60}\n")
    
    # Sort by GPU utilization (lowest first)
    underutilized_jobs.sort(key=lambda x: x["gpu_util_percent"])
    
    for i, job in enumerate(underutilized_jobs, 1):
        print(f"{i}. Job {job['job_id']} on {job['cluster']}")
        print(f"   User: {job['user']} | Partition: {job['partition']} | State: {job['state']}")
        print(f"   Duration: {job['duration_hours']} hours")
        print(f"   GPUs: {job['num_gpus']} | GPU Utilization: {job['gpu_util_percent']}% ⚠️")
        print(f"   CPU Load: {job['cpu_load_avg']} | Memory: {job['mem_used_max_gb']} GB")
        print(f"   Started: {job['start_time']}")
        print()
    
    # Save to JSON file
    output_file = "underutilized_gpu_jobs.json"
    with open(output_file, "w") as f:
        json.dump(underutilized_jobs, f, indent=2)
    print(f"💾 Results saved to: {output_file}")
else:
    print("✅ No underutilized GPU jobs found!")
