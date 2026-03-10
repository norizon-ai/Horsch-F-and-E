# Kubernetes Deployment - Auto-Scaling Celery Workers

## Architecture

This deployment uses **Horizontal Pod Autoscaling (HPA)** to automatically scale Celery workers based on system load.

### Scaling Triggers

**Option 1: Standard HPA (CPU/Memory)**
- Scales based on CPU utilization (>70%)
- Scales based on memory utilization (>80%)
- Built into Kubernetes, no additional tools needed

**Option 2: KEDA (Queue-based) - RECOMMENDED**
- Scales based on **Redis queue depth** (jobs waiting)
- Ideal for job processing workloads
- Requires KEDA installation (one-time setup)

### Scaling Behavior

| Condition | Min Workers | Max Workers | Scale Up Time | Scale Down Time |
|-----------|-------------|-------------|---------------|-----------------|
| Idle      | 1           | 10          | Immediate     | 5 minutes       |
| Busy      | Auto-scaled | 10          | 15 seconds    | 5 minutes       |

**Scale Up Policy:**
- Doubles workers every 15s OR adds 2 workers (whichever is smaller)
- Example: 1 → 2 → 4 → 6 → 8 → 10 workers in ~60 seconds

**Scale Down Policy:**
- Reduces by 50% every 60s after 5-minute stabilization
- Example: 10 → 5 → 3 → 2 → 1 workers over ~10 minutes

---

## Prerequisites

### 1. Kubernetes Cluster
```bash
# AWS EKS
eksctl create cluster --name norizon-prod --region eu-central-1

# Or Azure AKS
az aks create --name norizon-prod --resource-group norizon-rg
```

### 2. Install KEDA (for queue-based scaling)
```bash
kubectl apply -f https://github.com/kedacore/keda/releases/download/v2.12.0/keda-2.12.0.yaml
```

### 3. Create Namespace
```bash
kubectl create namespace norizon
```

### 4. Create Secrets
```bash
# Deepgram API Key
kubectl create secret generic deepgram-secrets \
  --from-literal=api-key=$DEEPGRAM_API_KEY \
  -n norizon

# OpenAI API Key
kubectl create secret generic openai-secrets \
  --from-literal=api-key=$OPENAI_API_KEY \
  -n norizon

# S3 Credentials
kubectl create secret generic s3-secrets \
  --from-literal=access-key=$AWS_ACCESS_KEY_ID \
  --from-literal=secret-key=$AWS_SECRET_ACCESS_KEY \
  -n norizon
```

---

## Deployment

### Deploy Celery Workers
```bash
kubectl apply -f celery-worker-deployment.yaml
```

### Enable Auto-Scaling

**Option 1: Standard HPA (CPU/Memory)**
```bash
kubectl apply -f celery-worker-hpa.yaml
```

**Option 2: KEDA (Queue-based) - RECOMMENDED**
```bash
# Deploy both HPA and KEDA
kubectl apply -f celery-worker-hpa.yaml
```

---

## Testing

### 1. Check Initial State
```bash
# View worker pods
kubectl get pods -n norizon -l app=celery-worker

# View HPA status
kubectl get hpa -n norizon

# View KEDA scaler (if using KEDA)
kubectl get scaledobject -n norizon
```

### 2. Simulate Load
```bash
# Submit 50 jobs to test scaling
for i in {1..50}; do
  curl -X POST http://api.norizon.ai/api/v1/transcribe/job-$i/process \
    -H "Content-Type: application/json" \
    -d '{"file_path": "/uploads/test-meeting.m4a", "glossary": []}'
  sleep 0.5
done
```

### 3. Watch Auto-Scaling
```bash
# Watch pods scale up
kubectl get pods -n norizon -l app=celery-worker -w

# Watch HPA metrics
kubectl get hpa celery-worker-hpa -n norizon -w

# View scaling events
kubectl describe hpa celery-worker-hpa -n norizon
```

### 4. Expected Behavior
```
Time    | Queue Depth | Workers | Action
--------|-------------|---------|-------------------------
0s      | 0           | 1       | Idle state
10s     | 50          | 1 → 2   | Scale up (queue detected)
25s     | 48          | 2 → 4   | Scale up (still busy)
40s     | 40          | 4 → 6   | Scale up (still busy)
60s     | 20          | 6 → 8   | Scale up
90s     | 5           | 8       | Hold (stabilizing)
180s    | 0           | 8       | Hold (5min cooldown)
480s    | 0           | 8 → 4   | Scale down
540s    | 0           | 4 → 2   | Scale down
600s    | 0           | 2 → 1   | Scale down to min
```

---

## Monitoring

### View Logs
```bash
# All workers
kubectl logs -n norizon -l app=celery-worker --tail=100 -f

# Specific worker
kubectl logs -n norizon celery-worker-abc123 -f
```

### Check Metrics
```bash
# CPU/Memory usage
kubectl top pods -n norizon -l app=celery-worker

# HPA metrics
kubectl get hpa celery-worker-hpa -n norizon -o yaml

# KEDA metrics (if using KEDA)
kubectl get scaledobject celery-worker-scaler -n norizon -o yaml
```

### View Redis Queue
```bash
# Connect to Redis
kubectl exec -it redis-0 -n norizon -- redis-cli

# Check queue length
LLEN celery

# View pending jobs
LRANGE celery 0 -1
```

---

## Troubleshooting

### Workers Not Scaling Up
```bash
# Check HPA status
kubectl describe hpa celery-worker-hpa -n norizon

# Common issues:
# 1. Metrics server not installed
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# 2. Resource requests not set (required for HPA)
kubectl get deployment celery-worker -n norizon -o yaml | grep -A 5 resources

# 3. KEDA not installed (for queue-based scaling)
kubectl get pods -n keda
```

### Workers Not Scaling Down
```bash
# Check cooldown period (default 5 minutes)
kubectl get hpa celery-worker-hpa -n norizon -o yaml | grep stabilizationWindowSeconds

# Force scale down (for testing only)
kubectl scale deployment celery-worker -n norizon --replicas=1
```

### High API Costs
```bash
# Reduce max workers
kubectl patch hpa celery-worker-hpa -n norizon -p '{"spec":{"maxReplicas":5}}'

# Increase scale-up threshold (less aggressive)
kubectl patch scaledobject celery-worker-scaler -n norizon --type='json' \
  -p='[{"op": "replace", "path": "/spec/triggers/0/metadata/listLength", "value":"10"}]'
```

---

## Cost Optimization

### Development Environment
- **Min:** 1 worker (idle)
- **Max:** 3 workers (peak)
- **Cost:** ~$50-150/month

### Production Environment
- **Min:** 2 workers (HA)
- **Max:** 10 workers (peak)
- **Cost:** ~$200-800/month

### Recommendations
1. Use KEDA queue-based scaling (more accurate than CPU)
2. Set `minReplicas=1` for non-critical workloads
3. Set `maxReplicas=10` to prevent runaway costs
4. Monitor Deepgram API costs (grows linearly with workers)
5. Use spot instances for workers (60% cheaper)

---

## Production Checklist

- [ ] KEDA installed and working
- [ ] Secrets created (Deepgram, OpenAI, S3)
- [ ] Resource limits set (CPU/memory)
- [ ] Health checks configured
- [ ] Monitoring/alerting enabled
- [ ] Auto-scaling tested under load
- [ ] Cost alerts configured
- [ ] Backup Redis to prevent queue loss
