import mlflow

experiment_name = "Ridge"
entry_point = "Training"

mlflow.set_tracking_uri("http://ec2-34-228-81-1.compute-1.amazonaws.com:5000/")

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    experiment_name=experiment_name,
    env_manager="conda"
)