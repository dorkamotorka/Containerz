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
