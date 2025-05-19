from prometheus_client import start_http_server, Counter
import time

# Define the metric
total_reviews = Counter('total_reviews', 'Total number of reviews processed')

def process_review():
    # Your logic to process a review
    total_reviews.inc()  # Increment the counter by 1

if __name__ == '__main__':
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    while True:
        process_review()
        time.sleep(1)
