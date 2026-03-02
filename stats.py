class Stats:
    def __init__(self):
        self.total_requests = 0
        self.total_latency = 0

    def update(self, latency):
        self.total_requests += 1
        self.total_latency += latency

    def report(self):
        if self.total_requests == 0:
            return "No data yet"
        avg_latency = self.total_latency / self.total_requests
        return f"Requests: {self.total_requests} | Avg Latency: {avg_latency:.4f}s"
