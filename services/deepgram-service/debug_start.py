import sys
import traceback

print("DEBUG: Starting import...", flush=True)
try:
    print("DEBUG: 1) Importing config...", flush=True)
    from src.config import settings
    print(f"DEBUG: 2) Config loaded OK", flush=True)
    
    print("DEBUG: 3) Importing celery_app...", flush=True)
    from src.celery_app import celery_app
    print(f"DEBUG: 4) Celery app loaded OK", flush=True)
    
    print("DEBUG: 5) Importing health API...", flush=True)
    from src.api import health
    print(f"DEBUG: 6) Health API loaded OK", flush=True)
    
    print("DEBUG: 7) Importing transcribe API...", flush=True)
    from src.api import transcribe
    print(f"DEBUG: 8) Transcribe API loaded OK", flush=True)
    
    print("DEBUG: 9) Importing jobs API...", flush=True)
    from src.api import jobs
    print(f"DEBUG: 10) Jobs API loaded OK", flush=True)
    
    print("DEBUG: 11) Importing FastAPI app...", flush=True)
    from src.main import app
    print("DEBUG: 12) Main imported OK!", flush=True)
    
    print("DEBUG: 13) Starting uvicorn...", flush=True)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
except Exception as e:
    print(f"CRASH: {type(e).__name__}: {e}", flush=True)
    traceback.print_exc()
    sys.exit(1)
