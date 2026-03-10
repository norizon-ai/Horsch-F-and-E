# Magic Link Authentication Implementation Plan

## Executive Summary

**Overall Complexity: MEDIUM-HIGH**
**Total Estimated Effort: 10-12 weeks**

The Norizon Research platform currently has **zero authentication infrastructure**. All state lives in browser localStorage, and services use in-memory storage. This plan covers implementing email-based magic link authentication with cross-device session persistence.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    FRONTEND (SvelteKit)                          │
│  Login → Email Input → Magic Link Sent → Verify → Dashboard     │
│  authStore.ts │ AuthGuard.svelte │ Session Management UI        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    AUTH SERVICE (workflow-service)               │
│  POST /auth/login  │  GET /auth/verify  │  POST /auth/refresh   │
│  Auth Middleware   │  Rate Limiting     │  CSRF Protection      │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    INFRASTRUCTURE                                │
│  PostgreSQL (users, sessions, audit)  │  Redis (rate limits)    │
│  SMTP/SendGrid (email)                │  Prometheus (metrics)   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Foundation (Weeks 1-3)

### Objective
Build the core authentication infrastructure: database schema, auth service, email delivery, and JWT token management.

### Database Schema

**New tables in PostgreSQL:**

```sql
-- Auth users (separate from existing tier0 users)
CREATE TABLE auth_users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email TEXT NOT NULL UNIQUE,
    email_verified BOOLEAN DEFAULT FALSE,
    display_name TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    last_login_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Magic link tokens (15-min expiry, one-time use)
CREATE TABLE magic_links (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth_users(id) ON DELETE CASCADE,
    token_hash TEXT NOT NULL UNIQUE,  -- SHA256, not plaintext
    expires_at TIMESTAMPTZ NOT NULL,
    used_at TIMESTAMPTZ,
    ip_address INET,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Active sessions (30-day expiry)
CREATE TABLE auth_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth_users(id) ON DELETE CASCADE,
    refresh_token_hash TEXT NOT NULL UNIQUE,
    expires_at TIMESTAMPTZ NOT NULL,
    revoked_at TIMESTAMPTZ,
    ip_address INET,
    user_agent TEXT,
    device_info JSONB DEFAULT '{}',
    last_activity_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Files to Create

| File | Purpose |
|------|---------|
| `services/workflow-service/migrations/001_auth_tables.sql` | Database schema |
| `services/workflow-service/app/db/__init__.py` | DB module exports |
| `services/workflow-service/app/db/connection.py` | Async SQLAlchemy setup |
| `services/workflow-service/app/db/models.py` | SQLAlchemy ORM models |
| `services/workflow-service/app/services/auth_service.py` | Magic link logic |
| `services/workflow-service/app/services/email_service.py` | SMTP/SendGrid abstraction |
| `services/workflow-service/app/services/token_service.py` | JWT generation/validation |
| `services/workflow-service/app/routers/auth.py` | Auth API endpoints |

### Files to Modify

| File | Changes |
|------|---------|
| `services/workflow-service/app/config.py` | Add database_url, jwt_secret, email settings |
| `services/workflow-service/requirements.txt` | Add asyncpg, sqlalchemy, PyJWT, aiosmtplib |
| `services/norizon-research/docker-compose.dev.yml` | Add PostgreSQL and Redis services |

### API Endpoints

```
POST /auth/login           # Request magic link (email input)
GET  /auth/verify          # Verify magic link token, create session
POST /auth/refresh         # Refresh access token
POST /auth/logout          # Invalidate session
GET  /auth/me              # Get current user info
GET  /auth/sessions        # List active sessions
DELETE /auth/sessions/{id} # Revoke specific session
```

### Security Considerations

- Magic link tokens: 256-bit entropy (`secrets.token_urlsafe(32)`)
- Tokens stored as SHA256 hash, never plaintext
- 15-minute expiry, single use
- Rate limit: 5 magic links per email per hour
- JWT access tokens: 15-minute expiry
- Refresh tokens: 30-day expiry with rotation

---

## Phase 2: Frontend Integration (Weeks 4-5)

### Objective
Build the login UI, auth state management, and route protection in the SvelteKit frontend.

### Files to Create

| File | Purpose |
|------|---------|
| `frontend/src/lib/stores/authStore.ts` | Auth state management |
| `frontend/src/lib/api/authApi.ts` | API client for auth endpoints |
| `frontend/src/routes/login/+page.svelte` | Email input form |
| `frontend/src/routes/auth/verify/+page.svelte` | Token verification page |
| `frontend/src/lib/components/AuthGuard.svelte` | Route protection component |

### Files to Modify

| File | Changes |
|------|---------|
| `frontend/src/routes/+layout.svelte` | Initialize auth store, add auth guards |
| `frontend/src/lib/api/searchApi.ts` | Add Authorization header to requests |
| `frontend/src/lib/api/workflowApi.ts` | Add Authorization header to requests |
| `frontend/src/lib/types/index.ts` | Add User, AuthState, AuthTokens types |
| `frontend/src/lib/i18n/locales/en.json` | Add auth-related translations |
| `frontend/src/lib/i18n/locales/de.json` | Add auth-related translations (German) |

### Auth Store Interface

```typescript
interface AuthState {
  user: User | null;
  accessToken: string | null;
  refreshToken: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  expiresAt: number | null;
}

export const authStore = {
  init(): void;                    // Load from localStorage
  setUser(user, tokens): void;     // After successful login
  logout(): void;                  // Clear auth state
  refreshSession(): Promise<boolean>;
  getAccessToken(): string | null;
};
```

### User Flow

1. User navigates to `/login`
2. Enters email, submits form
3. Backend sends magic link email
4. User clicks link → `/auth/verify?token=xxx`
5. Frontend calls API to verify token
6. On success: set auth state, redirect to `/`
7. On failure: show error, link to request new magic link

---

## Phase 3: Service Integration (Weeks 6-7)

### Objective
Add authentication middleware to all backend services with consistent token validation.

### Services to Update

| Service | Port | Changes |
|---------|------|---------|
| workflow-service | 8001 | Add auth middleware, protect all endpoints |
| transcription-service | 8002 | Add auth middleware for internal endpoints |
| confluence-publisher | 8003 | Add auth middleware for internal endpoints |

### Shared Auth Module

Create `shared/auth/` directory with:

```
shared/auth/
├── middleware.py      # FastAPI middleware for JWT validation
├── dependencies.py    # Depends() for route-level auth
├── models.py          # TokenClaims, AuthenticatedUser
├── config.py          # Auth settings
└── service_auth.py    # Service-to-service authentication
```

### Endpoint Classification

**Public (no auth):**
- `GET /health`, `/healthz`, `/readyz`
- `GET /docs`, `/redoc`, `/openapi.json`

**Protected (user auth required):**
- All `/api/v1/*` endpoints

**Internal (service auth required):**
- `POST /internal/*` endpoints (service-to-service calls)

### Service-to-Service Auth

Use `X-Service-Auth` header with shared secret:
```
X-Service-Auth: workflow-service:shared-secret
```

---

## Phase 4: Data Migration (Weeks 8-10)

### Objective
Replace localStorage with server-side storage for cross-device session persistence.

### Database Schema Additions

```sql
-- User chat sessions
CREATE TABLE user_chat_sessions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES auth_users(id) ON DELETE CASCADE,
    session_id TEXT NOT NULL,
    title TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, session_id)
);

-- Chat messages (normalized)
CREATE TABLE user_chat_messages (
    id UUID PRIMARY KEY,
    session_id UUID REFERENCES user_chat_sessions(id) ON DELETE CASCADE,
    message_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    sources JSONB DEFAULT '[]',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Workflow states
CREATE TABLE user_workflow_states (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES auth_users(id) ON DELETE CASCADE,
    job_id TEXT NOT NULL,
    current_step INTEGER NOT NULL,
    status TEXT NOT NULL,
    file_info JSONB,
    speakers JSONB DEFAULT '[]',
    protocol JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, job_id)
);
```

### API Endpoints

```
# Sessions
POST   /api/sessions                    # Create session
GET    /api/sessions                    # List user's sessions
GET    /api/sessions/{id}               # Get session with messages
PUT    /api/sessions/{id}               # Update session
DELETE /api/sessions/{id}               # Delete session
POST   /api/sessions/{id}/messages      # Add message
POST   /api/sessions/migrate            # Migrate localStorage data

# Workflows
GET    /api/workflows                   # List user's workflows
GET    /api/workflows/{job_id}          # Get workflow state
PUT    /api/workflows/{job_id}          # Update workflow state
POST   /api/workflows/migrate           # Migrate localStorage data
```

### Store Refactoring

**chatStore.ts changes:**
1. Initialize from server first, fallback to localStorage
2. Sync changes to server asynchronously
3. Handle offline mode with localStorage fallback
4. Migration modal on first authenticated login

**workflowStore.ts changes:**
1. Load from server when authenticated
2. Sync state changes to server
3. Fallback to localStorage when offline

### Migration Flow

1. User logs in (first time with existing localStorage data)
2. Show migration modal: "Found X sessions, Y workflows"
3. User clicks "Sync to Account"
4. POST to `/api/sessions/migrate` and `/api/workflows/migrate`
5. Clear localStorage on success
6. Show confirmation

---

## Phase 5: Hardening (Weeks 11-12)

### Objective
Production security hardening: rate limiting, CSRF, security headers, audit logging, GDPR compliance.

### Rate Limiting (Redis-based)

| Endpoint | Limit | Window |
|----------|-------|--------|
| `POST /auth/login` | 5 requests | 15 min |
| `POST /auth/magic-link` | 3 requests | 60 min |
| `POST /jobs` | 20 requests | 1 min |
| Global API | 100 requests | 1 min |

### CSRF Protection

- Double Submit Cookie pattern with signed tokens
- Exempt Bearer token auth (API-only)
- Token rotation every 30 minutes

### Security Headers

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
Content-Security-Policy: default-src 'self'; ...
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

### Audit Logging

**Events to log:**
- login_success, login_failed
- logout, session_revoked
- password_reset_requested
- data_export_requested, data_deletion_requested

**Schema:**
```sql
CREATE TABLE auth_audit_log (
    id UUID PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    user_id UUID REFERENCES auth_users(id),
    ip_address INET NOT NULL,
    user_agent TEXT,
    event_data JSONB,
    success BOOLEAN NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    retention_expires_at TIMESTAMPTZ DEFAULT NOW() + INTERVAL '2 years'
);
```

### GDPR Endpoints

```
POST /api/gdpr/export     # Request data export
GET  /api/gdpr/export/{id} # Check export status
POST /api/gdpr/delete     # Request account deletion
DELETE /api/gdpr/delete/{id} # Cancel deletion
GET  /api/gdpr/consent    # Get consent status
PUT  /api/gdpr/consent    # Update consent
```

### Session Management UI

Add `/settings/sessions` page:
- List all active sessions (device, browser, location)
- "Current session" badge
- Revoke individual sessions
- "Revoke all other sessions" button

---

## Infrastructure Changes

### docker-compose.dev.yml Additions

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: norizon
      POSTGRES_USER: norizon
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./migrations:/docker-entrypoint-initdb.d:ro

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
```

### Environment Variables

```env
# Database
WORKFLOW_DATABASE_URL=postgresql+asyncpg://norizon:password@postgres:5432/norizon

# JWT
WORKFLOW_JWT_SECRET_KEY=your-256-bit-secret-key
WORKFLOW_ACCESS_TOKEN_EXPIRE_MINUTES=15
WORKFLOW_REFRESH_TOKEN_EXPIRE_DAYS=30

# Email (SMTP)
WORKFLOW_EMAIL_PROVIDER=smtp
WORKFLOW_SMTP_HOST=smtp.example.com
WORKFLOW_SMTP_PORT=587
WORKFLOW_SMTP_USERNAME=...
WORKFLOW_SMTP_PASSWORD=...
WORKFLOW_EMAIL_FROM_ADDRESS=noreply@norizon.ai

# Redis
WORKFLOW_REDIS_URL=redis://redis:6379/1
```

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Breaking existing localStorage users | HIGH | Migration modal, preserve data on failure |
| Email deliverability in corporate env | MEDIUM | Support multiple providers, test with customer domains |
| Token security | HIGH | httpOnly cookies, refresh rotation, short expiry |
| Multi-tenant data isolation | HIGH | Row-level security, strict authorization |
| GDPR compliance | MEDIUM | Clear retention policies, right to deletion |

---

## Testing Strategy

### Unit Tests
- Auth service: token generation, magic link validation
- Rate limiter: sliding window algorithm
- CSRF: token generation/validation

### Integration Tests
- Full login flow: email → magic link → session
- Token refresh cycle
- Session revocation
- Data migration

### E2E Tests
- Login from multiple devices
- Cross-device session persistence
- Session management UI
- GDPR data export/deletion

---

## Verification Steps

After implementation, verify:

1. **Phase 1**: Can create user, send magic link email, verify token, get JWT
2. **Phase 2**: Login UI works, auth state persists, routes protected
3. **Phase 3**: All services require auth, service-to-service calls work
4. **Phase 4**: Data syncs across devices, migration works, offline fallback
5. **Phase 5**: Rate limits enforced, CSRF working, audit logs captured

### Manual Testing Checklist

- [ ] Register new user via magic link
- [ ] Login from different browser/device
- [ ] See same chat sessions on both devices
- [ ] Revoke session from one device
- [ ] Verify other device is logged out
- [ ] Request data export, verify contents
- [ ] Request account deletion, verify data removed
- [ ] Trigger rate limit, verify 429 response
- [ ] Check audit log for login events

---

## Critical Files Summary

### Backend (workflow-service)
- `app/main.py` - Add middleware stack
- `app/config.py` - Auth configuration
- `app/db/` - Database connection and models
- `app/services/auth_service.py` - Core auth logic
- `app/routers/auth.py` - Auth API endpoints
- `app/middleware/` - Rate limiting, CSRF, security headers

### Frontend (norizon-research/frontend)
- `src/lib/stores/authStore.ts` - Auth state
- `src/lib/api/authApi.ts` - Auth API client
- `src/routes/login/+page.svelte` - Login page
- `src/routes/auth/verify/+page.svelte` - Verification page
- `src/routes/+layout.svelte` - Auth initialization

### Infrastructure
- `docker-compose.dev.yml` - PostgreSQL, Redis
- `migrations/*.sql` - Database schema
