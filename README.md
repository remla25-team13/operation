# Operation
This repository contains code for composing our services together, alongside additional information and collaboration references.

## Running
Instructions on how to use `lib-ml`, `lib-version`, `app-service`, `app-frontend`, and `model-service` can be found in their respective repositories. Additionally, the trained models can be found as a GitHub artifact in `model-training`.

### Running with Docker
To run the latest image releases, simply execute the following command:

```bash
docker compose up --build
```

For development: but make sure you have all the repo's in one folder. 

```bash
docker compose -f docker-compose.dev.yml up --build
```

## HELM
running helm can be done by having a kubernetes cluster active and inputting the following command
helm install ./helm-chart --generate-name OR
helm install team10-release ./helm-chart

## Kubernetes ConfigMap and Secret Usage

- The deployment uses a Secret (`app-auth-token`) to provide sensitive data (auth token) to the app-service.
- The deployment uses a ConfigMap (`app-config`) to provide non-sensitive configuration (model service URLs) as environment variables.

## Pointers to relevant files that help outsiders understand the code base.
You can find our Activity feedback at https://github.com/remla25-team13/operation/blob/main/ACTIVITY.md

## A list of all relevant repositories for the project.
- lib-ml - https://github.com/remla25-team13/lib-ml
- lib-version - https://github.com/remla25-team13/lib-version
- app-service - https://github.com/remla25-team13/app-service
- app-frontned - https://github.com/remla25-team13/app-frontend
- model-service - https://github.com/remla25-team13/model-service

## Progress log
**Deadline 06/05/2025** We worked on getting the individual repositories set-up correctly but currently do not have the full app working. The individual components work we we have yet to integrate everything.

**Deadline 13/05/2025** We worked on getting assignment 1 to an excellent state and made an effort to get as far as possible with assignment 2, we are currently at step 20

## Grafana

This section explains how you can install **Grafana** and **Prometheus** locally on your Mac  
and connect them to visualize your application metrics.

### 1. Install Grafana

#### On Mac (using Homebrew)
```bash
brew install grafana
brew services start grafana
```

- Access Grafana at [http://localhost:3000](http://localhost:3000)
- Login with:
  - **Username**: `admin`
  - **Password**: `admin` (you'll be asked to change it)

### 2. Install Prometheus

#### On Mac (using Homebrew)
```bash
brew install prometheus
brew services start prometheus
```

- Access Prometheus at [http://localhost:9090](http://localhost:9090)

> 💡 _Make sure Prometheus is correctly configured to scrape metrics from your application._

### 3. Connect Grafana to Prometheus

1. In Grafana, click **⚙️  Configuration > Data Sources**.
2. Click **Add data source** and choose **Prometheus**.
3. Set **URL** to `http://localhost:9090`.
4. Click **Save & Test**.

### 4. Import the Grafana Dashboard

1. In Grafana, click **+ > Import**.
2. Upload `grafana/dashboards/k8-dashboard.json` from this repository.
3. Select your Prometheus data source and click **Import**.