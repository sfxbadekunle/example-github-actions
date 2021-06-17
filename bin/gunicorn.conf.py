import multiprocessing
import os

bind = f"0.0.0.0:{os.getenv('PORT', 3000)}"
workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))