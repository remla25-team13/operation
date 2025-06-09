# Deployment
This repository contains documentation for the structure of our deployment.

Next to this repository there are are six additional repositories containing components of the full application.
#### A list of all relevant repositories for the project.
- lib-ml - https://github.com/remla25-team13/lib-ml
- lib-version - https://github.com/remla25-team13/lib-version
- app-service - https://github.com/remla25-team13/app-service
- app-frontend - https://github.com/remla25-team13/app-frontend
- model-service - https://github.com/remla25-team13/model-service
- model-training - https://github.com/remla25-team13/model-training

### Repository content
#### lib-ml 
This repository contains the shared pre-processing logic which is reused by both the model-training and model-service components.
The features are as follows:
- Cleans and normalizes input text
- Removes URLs and punctuation
- Shared between training and inferenc

#### lib-version
This repository contains a small utility library that provides version information at runtime which is used by app-service.
The features are as follows:
- Provides a VersionUtil class to programmatically retrieve the package version.
- Useful for system information in logs, debug output, or API responses.
- Version is automatically aligned with Git tags using package metadata.

#### app-service
This repository contains the backend app service our REMLA25 project. This is a Flask application which performs REST API calls to the model-service to access the model and returns corresponding results.
The service allows for the following API-Calls:
- `GET /` — Returns a greeting message from the app-service.
- `POST /create` — Performs a non-functional create operation.
- `GET /read` — Performs a non-functional read operation.
- `PUT /update` — Performs a non-functional update operation.
- `DELETE /delete` — Performs a non-functional delete operation.
- `GET /version/app-service` — Returns the version of the app-service.
- `GET /version/lib-version` — Returns the version of the `lib-version` library.
- `POST /predict` — Forwards a review to the model-service for sentiment prediction.
- `POST /submit` — Submits a review and correctness label for tracking model accuracy.
- `GET /metrics` — Returns Prometheus-compatible metrics such as prediction counts and model accuracy.

#### app-frontend
This repository contains the code for the Angular Frontend. This app is a standard angular app which implements a frontend to interact with the app-service api. It allows a user to sumbit a review and check the evaluation of the text by a model. THen the user can modify the prediction if it is incorrect.

Unique features are:
- The custom environment /environments/environment.ts
- The interaction with the app-service API

#### model-service
This repository contains the service through which we serve our model. This app is a Flask application which downloads the most recent model artifacts from model-training and serves it to facilitate the following calls from the app-service app:
- `GET /version/app-service` — Returns the version of the app-service.
- `POST /predict` — Forwards a review to the model-service for sentiment prediction.

#### model-training
This repository contains the machine learning training pipeline for sentiment analysis on restaurant reviews.

Features:
- Loads the historic restaurant reviews dataset.
- Preprocesses data using lib-ml.
- Trains and evaluates the sentiment model.
- Versions and releases the model for deployment.
- DVC pipeline
- ML testing 

#### operation
This repository contains code for composing our services together, alongside additional information and collaboration references.

### Deployment

#### Dockerized 
The bare-bones version of the app can be ran through docker using the following command:
`docker compose up --build`

##### System Overview
This system is composed of three Dockerized services orchestrated via Docker Compose:

###### Services
1. `app-frontend`
- Web-based user interface.
- **Image**: `ghcr.io/remla25-team13/app-frontend:latest`
- **Ports**: Exposes `4200` on the host.
- **Depends On**: `app-service`

2. `app-service`
- Backend API layer that communicates with the model.
- **Image**: `ghcr.io/remla25-team13/app-service:latest`
- **Environment Variables**:
  - `MODEL_SERVICE_URL`: URL of the `model-service`, built dynamically using `MODEL_SERVICE_PORT`.
- **Depends On**: `model-service`
- **Secrets**:
  - `auth_token`: Shared secret used for authentication with the `model-service`.

3. `model-service`
- Machine learning model service used for predictions.
- **Image**: `ghcr.io/remla25-team13/model-service:latest`
- **Environment Variables**:
  - `VERSION`: Model version
  - `MODE`: Set to `PROD`
  - `PORT`: Port number (value must be passed as `MODEL_SERVICE_PORT`)
- **Ports**: Exposes the port defined by `MODEL_SERVICE_PORT`
- **Secrets**:
  - `auth_token`: Same shared secret as used by `app-service`.

##### Secrets
###### auth_token
- Stored in `./auth_token.txt`
- Mounted into both `app-service` and `model-service` for authentication purposes.



#### Vagrant + Kubernetes
- The host shoud be running MacOS or Linux.
- The host should have virtualbox installed.
- The host should have Vagrant available.

The application can then be started by cloning our repository and using the following command:
`vagrant up`

##### the Vagrant File describes the following

This Vagrantfile defines a virtual environment consisting of one control node and multiple worker nodes, all provisioned with Ansible.

###### Configuration Summary
- **Number of Worker Nodes**: default of 2 configurable through the `NODES` parameter
- **Base Image**: bento/ubuntu-24.04
- **Provisioner**: Ansible
- **Provider**: VirtualBox

###### Ansible Provisioning
All nodes run a general setup via `general.yml`. Additional, role-specific playbooks are executed:
- `ctrl.yml` for the control node.
- `node.yml` for each worker.

###### Networking
- **Private Network IPs**: Assigned statically in the `192.168.56.100+` range.

###### Ansible Groups
- **Control Group**: `ctrl`
- **Worker Group**: `node-1`, `node-2`

###### Ansible Playbooks
- **General** This Ansible playbook provisions all nodes for Kubernetes by setting up SSH keys, disabling swap, enabling kernel modules, and configuring system networking. It installs necessary packages like `containerd`, `kubelet`, `kubeadm`, and `kubectl`, and applies custom containerd settings. It also configures `/etc/hosts` from a template and enables key system services.
- **Ctrl** This Ansible playbook sets up the Kubernetes control plane on the `ctrl` node. It initializes the cluster with `kubeadm`, sets up the kubeconfig for the `vagrant` user and Ansible host, and installs the Flannel CNI if it's not already present. It also installs Helm and the `helm-diff` plugin for managing charts.
- **Finalization** This Ansible playbook finalizes the Kubernetes cluster setup by installing key components. It sets up **MetalLB** for LoadBalancer support, **NGINX Ingress Controller**, and the **Kubernetes Dashboard** using Helm. It also installs **Istio** with a custom IP and deploys **Prometheus** for monitoring, including a custom `ServiceMonitor` for `app-service`. 
- **Node** This Ansible playbook joins all worker nodes to the Kubernetes cluster by running the `kubeadm join` command obtained from the controller node. It ensures the `vagrant` user has the appropriate kubeconfig by creating the `.kube` directory and copying the `kubelet.conf` for access to cluster resources.