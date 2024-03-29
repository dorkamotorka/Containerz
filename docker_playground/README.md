# Run Containers in Sequence

The goal of this example is to test, how can we run containers in a specific order. 
This is simple in the case of docker-compose, but the question is whether we can achieve the same thing on Kubernetes.

## Preparing containers

First build the two containers using (note the dots at the end!):

	docker build -t first --build-arg MY_STRING="This is the first container" .
	docker build -t second --build-arg MY_STRING="This is the second container" .

You should be able to run both using:

	docker run first
	docker run second

## Setting up Kubernetes

There are many Kubernetes distributions, and I won't go through the installation steps, because there are many good articles already out there. 
If you're new to Kubernetes, I suggest looking into `microk8s` which I believe is the most user-friendly to get started.
Once you have your cluster running and got a bit comfortable with the `kubectl` let's try to deploy our previously build containers using different configurations.

First, let's apply the configuration in `deployment-1.yml` using:

	kubectl apply -f deployment-1.yml

When you run the deployment a couple of times, you're gonna notice, that the containers gets spawn in the order they are defined, but the second container does not await the end of execution of the first container. Instead it gets executed soon after the first container, even if it was unsuccesful.

This can be desired or not but at this point, it might be neccesary to add up to the initial goal. We not only want to execute the containers in a specific order, but also have them succesfuly terminate in order as well. 
And if the first container would crash, the second container shouldn't even be executed, because it's state could potentially depend upon the succesful execution of the first container.

This is achieved using the configuration in `deployment-2.yml`, which you can execute using:

	kubectl apply -f deployment-2.yml

In both deployments you can debug and confirm the above theory by looking into the log output of each container using:

	kubectl logs <deployment-name> -c <container-name>

By the execution time, you should be able to easily determine when the containers where executed and how.
