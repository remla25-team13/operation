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

#### Vagrant + Kubernetes
- The host shoud be running MacOS or Linux.
- The host should have virtualbox installed.
- The host should have Vagrant available.

The application can then be started by cloning our repository and using the following command:
`vagrant up`