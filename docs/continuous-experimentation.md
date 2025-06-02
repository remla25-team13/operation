We chose to experiment with a new model type. Currently, we use a Gaussian Naive Bayes classifier to determine a review's stance. However, our review data is discrete, meaning that a Multinomial classifier might be more appropriate as it can handle discrete data better. As such, we pose the following hypothesis:

>A Multinomial Naive Bayes classifier outperforms a Gaussian Naive Bayes classifier given the same training conditions. 

We use the default parameters for both models and provide them with the same data and training setup. We use A/B testing to test our hypothesis. We set up two versions of our `model-service` service, each hosting a different model. Then, we redirect users to one of the two versions when they issue a `/predict` request to `app-service.` Under the hood, `app-service` randomly picks one of the two model services and records the relevant statistics for that model. The statistics are then exported and accessible through Prometheus.

We handle configuring the `model-service` endpoints, model loading, and A/B switch probability through environment variables.  