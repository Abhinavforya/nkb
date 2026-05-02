#!/usr/bin/env bash
set -e
# If PORT is set (Render / production), use gunicorn with Uvicorn worker
if [ -n "$PORT" ]; then
	exec gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
else
	# Local development fallback with autoreload
	exec uvicorn main:app --reload --host 127.0.0.1 --port 8000
fi
