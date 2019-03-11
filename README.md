## docker-python-flask-api

This is a sample application in python which is created into a docker container and deployed to ElasticBeanstalk using CICD pipeline.

## Important

This demo demonstrates how we can use the DEV Flask WEB application having the python API calls to deploy on docker containers with the help of Dockerfile.dev and once validated/verified, we can later with the help of Dockerfile move the PROD code to production pipeline.

# Another Enhancement

Later we enhanced the code by adding the **Dockerrun.aws.json.**
**This section describes how to prepare your Docker image and container for deployment to Elastic Beanstalk. Any web application that you deploy to Elastic Beanstalk in a single container Docker environment must include a Dockerfile or a Dockerrun.aws.json file.**

**A Dockerrun.aws.json file is an Elastic Beanstalk-specific file that specifies how to deploy the set of Docker containers as an EB application. We use Dockerrun.aws.json for multicontainer docker environment.**
### This in essense somewhat similar to docker-compose.yml which is used to multi container deployment.

**docker-compose.yml** is used for **DEV/TEST Env** deployments and **Dockerrun.aws.json** is used for **PROD** deployments.

**Major Benefit of Dockerrun.aws.json**

With the use of **Dockerrun.aws.json.** we can remove the overhead of building the image all over again. Because when we do not use **Dockerrun.aws.json.**, we end up building Image with Travis CI along with running the image to test the success or failure and then later when we **deploy** in **EB** that again first it builds the image and then deploys and hence devaiating from its main task of application hosting/processing requests.

## Requirements

This requires following softwares -

Flask

boto3

docker

## Other requirements include :-

Travis CI

Github 

AWS ElasticBeanstalk -- Make sure to update the default role created with elastic beanstalk for your boto3 API calls to work.