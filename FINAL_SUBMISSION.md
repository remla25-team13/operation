# Final submission REMLA

- [Final submission REMLA](#final-submission-remla)
  - [All our repositories](#all-our-repositories)
  - [How to run our code with kubernetes](#how-to-run-our-code-with-kubernetes)
    - [Grafana](#grafana)
  - [How to run the code with docker](#how-to-run-the-code-with-docker)
  - [Documentation](#documentation)

## All our repositories
Here you can find all our reposities: https://github.com/orgs/remla25-team13/repositories

 Click [here](https://github.com/remla25-team13/operation/blob/main/docs/deployment.md#repository-content) to read about the content of all the repositories.

## How to run our code with kubernetes

```bash
vagrant up

export KUBECONFIG=ansible/playbooks/kubeconfig/admin-ctrl.conf

ansible-playbook -u vagrant -i 192.168.56.100, ansible/playbooks/finalization.yml

helm install helm-chart/ --generate-name

# /etc/hosts
192.168.56.90 dashboard.local grafana.local prometheus.local
192.168.56.91 app.local

kubectl -n kubernetes-dashboard create token admin-user

vagrant destroy -f
```

Do not forget the .gdrive-credentials.json in helm-chart folder. Altough, we will include it already in the submission.

You can now access:
- http://dashboard.local
- http://grafana.local
- http://prometheus.local
- http://app.local
- http://app.local/api/

grafana (default credentials):
- admin
- prom-admin

### Grafana

1. In Grafana, click **+ > Import**.
2. Upload `grafana/dashboards/team13.json` from this repository.
3. Select your Prometheus data source and click **Import**.

## How to run the code with docker
Copy the .env.example to .env and fill the DVC credentials. For the submission we will already add the .env.

Now you can do:
```bash
docker compose up --build
docker compose down
```

## Documentation
For documentation please check ```docs/``` folder. Especially the ```docs/deployment.md``` should give you a lot of insight in how our project architecture works.

Also check the README of every repository for more specific information.

- operation - https://github.com/remla25-team13/operation
- app-frontend - https://github.com/remla25-team13/app-frontend
- app-service - https://github.com/remla25-team13/app-service
- model-service - https://github.com/remla25-team13/model-service
- model-training - https://github.com/remla25-team13/model-training
- lib-ml - https://github.com/remla25-team13/lib-ml
- lib-version - https://github.com/remla25-team13/lib-version

We recommend to read the model-training README.
