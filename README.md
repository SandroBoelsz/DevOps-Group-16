# DevOps-Group-16




# CI/CD Pipeline for LifeWatch Application
This section outlines the Continuous Integration and Continuous Deployment (CI/CD) process for building, pushing, and deploying the LifeWatch application to Amazon Elastic Container Registry (ECR) and Elastic Kubernetes Service (EKS) using GitHub Actions.

## Overview

- **Trigger**: The pipeline runs on pushes to the `main` branche.
- **Environment**: AWS in the `eu-central-1` region.
- **Components**:
  - Builds a Docker image from the `workflow-data-replication-api` directory.
  - Pushes the image to Amazon ECR.
  - Deploys the image to an EKS cluster using Kubernetes manifests.

## Prerequisites

1. **AWS Credentials**: 
   - Store `AWS_ACCESS_KEY` and `AWS_ACCESS_KEY_SECRET` as GitHub Secrets in your repository.
2. **ECR Repository**: An ECR repository named `lifewatch` must exist in your AWS account.
3. **EKS Cluster**: A cluster named `Group16EKSCluster` must be set up in the `eu-central-1` region.
4. **Kubernetes Manifests**: The `manifests/` directory should contain `lifewatch-deployment.yaml` and `lifewatch-service.yaml`.

## Pipeline Steps

### 1. Trigger
The pipeline is triggered on a `push` event to the `main` or `ci-cd-pipeline` branches.

### 2. Build and Push to ECR
- **Checkout Code**: Pulls the latest code from the repository.
- **Configure AWS Credentials**: Authenticates with AWS using the provided access key and secret.
- **Login to ECR**: Logs into the ECR registry.
- **Build and Push Docker Image**:
  - Builds the Docker image from the `workflow-data-replication-api` directory.
  - Tags the image as `ECR_REGISTRY/ECR_REPOSITORY:latest`.
  - Pushes the image to ECR.

### 3. Deploy to EKS
- **Update Kubeconfig**: Configures `kubectl` to connect to the `Group16EKSCluster` EKS cluster.
- **Apply Manifests**:
  - Deploys the application using `lifewatch-deployment.yaml`.
  - Exposes the application using `lifewatch-service.yaml`.

## Kubernetes Configuration

### Deployment (`lifewatch-deployment.yaml`)
- **Name**: `lifewatch-deployment`
- **Replicas**: 1
- **Container**:
  - Image: `ECR_REGISTRY/ECR_REPOSITORY:latest` (from ECR - is hardcoded in the yaml).
  - Port: `5000`
  - Pull Policy: `Always`
- **Strategy**: Rolling update with `maxSurge: 1` and `maxUnavailable: 1`.

### Service (`lifewatch-service.yaml`)
- **Name**: `lifewatch-service`
- **Type**: `LoadBalancer`
- **Port**: `5000` (mapped to container port `5000`).


## Things to note

- Access for Kubernetes requires IAM access entry on own `IAM user` and Access policy `AmazonEKSAdminPolicy`
- The loadbalancer and security group are automatically configured by the EKS service.
- In this case the loadbalancer is named `afd188729fa134b52937207f9fda48b5` and security group is `lifewatch-sg`.
  