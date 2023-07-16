import multiprocessing

from app import env

# Host and port
bind = env(
    "GUNICORN_BIND", cast=str, default="0.0.0.0:8000"
)  # pylint: disable=invalid-name

# Workers
worker_class = env(
    "GUNICORN_WORKER_CLASS", cast=str, default="uvicorn.workers.UvicornWorker"
)  # pylint: disable=invalid-name
workers_per_core = env(
    "GUNICORN_WORKERS_PER_CORE", cast=int, default=1
)  # pylint: disable=invalid-name
cores = multiprocessing.cpu_count() // 2  # pylint: disable=invalid-name
default_web_concurrency = workers_per_core * cores  # pylint: disable=invalid-name
default_web_concurrency = max(
    int(default_web_concurrency), 2
)  # pylint: disable=invalid-name
workers = (
    env("GUNICORN_WORKERS", cast=int, default=0) or default_web_concurrency
)  # pylint: disable=invalid-name

# Timeouts
keepalive = env("GUNICORN_KEEPALIVE", cast=int, default=5)  # pylint: disable=invalid-name
graceful_timeout = env(
    "GUNICORN_GRACEFUL_TIMEOUT", cast=int, default=120
)  # pylint: disable=invalid-name
timeout = env("GUNICORN_TIMEOUT", cast=int, default=120)  # pylint: disable=invalid-name

# Debug Gunicorn configurations
LOG_DATA = {
    "bind": bind,
    "worker_class": worker_class,
    "workers_per_core": workers_per_core,
    "cores": cores,
    "workers": workers,
    "keepalive": keepalive,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "wsgi_app": "app.main:app",
}
