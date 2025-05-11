## Repositories
operation: https://github.com/remla25-team13

model-training: https://github.com/remla25-team13/model-training/releases/tag/v0.0.8 model training works, we use the lib-ml repo for pre-processing and upload the artefacts of the generated files through github actions.
- model https://github.com/remla25-team13/model-training/actions/runs/14864990743/artifacts/3071785209
- vectorizer https://github.com/remla25-team13/model-training/actions/runs/14864990743/artifacts/3071785342

model-service: loads the model artefacts and serves it through a flask api

lib-ml: https://github.com/remla25-team13/lib-ml/releases/tag/v0.1.1 works as a package and is used by model-service and model-training as can be seen in their requirements.txt

lib-version: https://github.com/remla25-team13/lib-version/releases/tag/v0.0.1 implemented

app-frontend: angular app WIP.

app-service: angular app WIP.

## Comments for A1:
We worked on getting the individual repositories set-up correctly but currently do not have the full app working.
The individual components work we we have yet to integrate everything.