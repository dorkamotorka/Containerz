FROM alpine:latest

# Declare a build argument
ARG MY_STRING

# Set an environment variable with the value of the build argument
ENV MY_STRING_ENV $MY_STRING

# Echo the value of the environment variable when the container is run
CMD echo "$MY_STRING_ENV - Container execution time: $(date +%Y-%m-%d\ %H:%M:%S)"
