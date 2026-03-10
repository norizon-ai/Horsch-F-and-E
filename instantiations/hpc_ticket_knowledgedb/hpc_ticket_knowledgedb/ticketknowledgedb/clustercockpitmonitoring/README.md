# ClusterCockpit Monitoring Tools

Tools for analyzing GPU job utilization on HPC clusters using the ClusterCockpit API.

## Setup

1. **Create config file** with your JWT token:
   ```bash
   cp config.sh.example config.sh
   # Edit config.sh and add your JWT token
   ```

2. **Install Python dependencies**:
   ```bash
   pip install requests
   ```

## Scripts

### `find_underutilized_gpu_jobs.py`
Finds GPU jobs with low utilization in the last 3 days.

**Criteria:**
- Duration: > 2 hours
- GPU allocation: > 0 GPUs
- GPU utilization: < 70%

**Usage:**
```bash
bash run_analysis.sh
```

Or manually:
```bash
source config.sh
export CLUSTERCOCKPIT_JWT="$JWT"
python3 find_underutilized_gpu_jobs.py
```

**Output:**
- Console: Formatted list of underutilized jobs
- File: `underutilized_gpu_jobs.json` with full details

**Customization:**
Edit the script to adjust:
- `MIN_DURATION_HOURS = 2` - Minimum job duration
- `MAX_GPU_UTILIZATION = 70.0` - Maximum GPU utilization threshold
- `DAYS_LOOKBACK = 3` - How many days to look back
- `CLUSTERS = ["alex", "helma"]` - Which clusters to query

### Test Scripts

- `test_jobalex.sh` - Query Alex cluster jobs
- `test_jobuserapi_nojwt.sh` - Query Helma cluster jobs

## Configuration

**config.sh** contains:
- `JWT` - Authentication token for ClusterCockpit API
- `API_BASE_URL` - Base URL for the API

**Note:** `config.sh` is gitignored to prevent accidentally committing tokens.

## API Endpoints

Base URL: `https://monitoring.nhr.fau.de`

- `/userapi/jobs/` - Get jobs with filtering

**Parameters:**
- `cluster` - Cluster name (alex, helma, etc.)
- `state` - Job state (running, completed, failed)
- `start-time` - Time range (format: `{start_unix}-{end_unix}`)
- `user` - Filter by username
- `items-per-page` - Pagination limit

## Example Output

```
🔍 Searching for underutilized GPU jobs
📅 Time range: Last 3 days
⏱️  Min duration: 2 hours
📊 Max GPU utilization: 70%
============================================================

🖥️  Querying cluster: alex
  ✓ Found 150 jobs
🖥️  Querying cluster: helma
  ✓ Found 0 jobs

============================================================
📊 SUMMARY
============================================================
Total jobs checked: 150
Jobs with GPUs: 45
Underutilized GPU jobs: 12
============================================================

⚠️  UNDERUTILIZED GPU JOBS (GPU util < 70%)
============================================================

1. Job 138993 on alex
   User: v103fe18 | Partition: preempt | State: completed
   Duration: 5.2 hours
   GPUs: 4 | GPU Utilization: 0.0% ⚠️
   CPU Load: 1.93 | Memory: 38.81 GB
   Started: 2025-10-05 14:32:22
```

## Documentation

- [ClusterCockpit REST API](https://www.clustercockpit.org/docs/how-to-guides/userest/)
- [JWT Token Generation](https://www.clustercockpit.org/docs/how-to-guides/generatejwt/)
