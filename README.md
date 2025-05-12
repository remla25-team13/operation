# Operation
This repository contains code for composing our services together, alongside additional information and collaboration references.

## Running
Instructions on how to use `lib-ml`, `lib-version`, `app-service`, `app-frontend`, and `model-service` can be found in their respective repositories. Additionally, the trained models can be found as a GitHub artifact in `model-training`.

### Running with Docker
To run everything standalone, simply execute the following command:

```bash
docker compose up --build
```

For development: but make sure you have all the repo's in one folder. 

```bash
docker compose -f docker-compose.dev.yml up --build
```

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