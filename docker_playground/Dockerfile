FROM alpine:latest

# Declare a build argument
ARG MY_STRING

# Set an environment variable with the value of the build argument
ENV MY_STRING_ENV $MY_STRING

# Sleep for 5 second to distinguish the startup times of the containers
# Will make sense in the 2nd step of the tutorial
# Echo the value of the environment variable when the container is run
CMD sh -c 'sleep 5 && echo "$MY_STRING_ENV - Container execution time: $(date +%Y-%m-%d\ %H:%M:%S)"'
