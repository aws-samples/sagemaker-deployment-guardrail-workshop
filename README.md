# SageMaker Inference and Deployment Guardrail Workshop
## Introduction
This workshop is intended for customers who are interested in learning how to effectively leverage Amazon SageMaker service to deploy an LLM for inference and manage the continuous deployment process for updating models in production. 

The workshop comprises a set of use cases that will help deployment features offered in SageMaker.

The use cases can be found in the following: 

**Lab 1** - This lab deploys an LLM called [SQLCoder](https://huggingface.co/defog/sqlcoder) from Huggingface to SageMaker using Deep Learning Container LMI and runs inferences on the deployed endpoint. 

**Lab 2** - This lab focuses on a use case that involves building of an inference pipeline using multiple containers. The inference pipeline is hosted behind a single endpoint, leveraging [SageMaker Serial Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) feature to simply the end to end deployment and request orchestrations. 

**Lab 3** - This lab focuses on enabling MLOps engineers to simplify CI/CD deployment for updating a model. Using a fully managed deployment option supported in [SageMaker Deployment Guardrail](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html), this lab walks through the steps for managing model updates using Canary deployment option. 

## Getting Started
Please refer to this [workshop studio](https://catalog.us-east-1.prod.workshops.aws/workshops/ef2ee096-275b-4c34-8ce0-1e85ea5e77c0/en-US) for detailed instructions on how to get started.
