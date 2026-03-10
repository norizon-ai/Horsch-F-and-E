# Quick Start - Nora Research with Proxy

## Issue: User Creation Required

DeepResearch requires a user account to be created before the proxy can authenticate. You need to create the `nora-proxy` user first.

## Quick Setup (5 minutes)

### Step 1: Create Proxy User in DeepResearch

1. **Access DeepResearch Web UI:**
   ```bash
   open http://localhost:5001
   ```

2. **Register the proxy user:**
   - Click on "Register" or create account
   - Username: `nora-proxy`
   - Password: `nora-proxy-2025`
   - Complete the registration

3. **Log out** after registration (the proxy will handle logins automatically)

### Step 2: Restart the Proxy

```bash
cd /Users/omariko/Documents/GitHub/tier-zero/services/norizon-research
docker-compose -f docker-compose.dev.yml restart proxy

# Verify login succeeded
docker logs norizon-proxy-dev | grep "Successfully logged in"
```

You should see: `✓ Successfully logged in to DeepResearch`

### Step 3: Start Frontend

```bash
cd frontend
npm run dev
```

### Step 4: Test!

Open http://localhost:5173 and try a research query!

---

## Alternative: Use Environment Variables for Different Credentials

If you want to use different credentials:

1. Edit `docker-compose.dev.yml`:
   ```yaml
   proxy:
     environment:
       - DEEPRESEARCH_USERNAME=your-username
       - DEEPRESEARCH_PASSWORD=your-password
   ```

2. Create that user in DeepResearch web UI

3. Restart proxy: `docker-compose -f docker-compose.dev.yml restart proxy`

---

## Troubleshooting

**Problem: Login still fails**
```bash
# Check if user exists
curl -X POST http://localhost:5001/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=nora-proxy&password=nora-proxy-2025&csrf_token=test"
```

If you get 401, the user doesn't exist yet - create it via the web UI.

**Problem: Can't access DeepResearch UI**
```bash
# Check if DeepResearch is running
docker ps | grep deepresearch

# Restart if needed
docker-compose -f docker-compose.dev.yml restart deepresearch

# Wait 30 seconds, then try again
```

**Problem: Frontend gets 404 errors**
```bash
# Check proxy is running and healthy
curl http://localhost:5002/health

# Check proxy logs
docker logs -f norizon-proxy-dev
```

---

## Current Architecture

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   Frontend   │─────▶│  Nora Proxy  │─────▶│ DeepResearch │
│  localhost:  │      │  (Logged in  │      │  (User DB:   │
│    5173      │      │   as nora-   │      │  nora-proxy) │
│              │      │   proxy)     │      │              │
└──────────────┘      └──────────────┘      └──────────────┘
```

The proxy:
1. ✓ Logs in automatically on startup
2. ✓ Maintains session cookies
3. ✓ Gets CSRF tokens for each request
4. ✓ Forwards queries to `/api/start_research`
5. ✓ Streams SSE responses back to frontend

Once the `nora-proxy` user is created, everything works automatically!
