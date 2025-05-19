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
helm install ./helm-chart --generate-name

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
