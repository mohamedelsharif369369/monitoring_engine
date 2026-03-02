# URL الهدف (يمكن تغييره لأي API قانوني)
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# إعدادات الأداء
CONCURRENT_REQUESTS = 200
REQUEST_TIMEOUT = 5  # seconds
MONITOR_INTERVAL = 2  # seconds

# إعدادات Redis و PostgreSQL
REDIS_URL = "redis://localhost:6379/0"
POSTGRES_DSN = "dbname=monitor user=postgres password=postgres host=localhost port=5432"
