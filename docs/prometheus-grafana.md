# Prometheus
Prometheus is a popular monitoring system and time series database. It periodically pings a predefined URL which exposes metrics (for example localhost:8000/metrics), collects the data, and enables exploration through its build in PromQL language.

In our project, we use Prometheus to support the our model type experiment. We expose metrics for both models, which we can easily query and explore through Prometheus.
# Grafana
Grafana is a visualization and monitoring platform. Typically, Grafana queries a database (like Prometheus) and exports the found metrics through its UI. Grafana also allows for custom UIs, such as the one we have developed for our experiment. 
