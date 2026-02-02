import requests
import sys

try:
    r = requests.get("http://localhost:8000/health/")
    if r.status_code == 200:
        sys.exit(0)  # healthy
    else:
        sys.exit(1)  # unhealthy
except:
    sys.exit(1)