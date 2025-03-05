# Development

### Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
cd workflow-data-replication-api
pip install -r requirements.txt
```
### Create a .env file
```bash
touch .env
```

Fill the .env file with the following content:
```bash
UVA_MINIO_API= # URL of the UvA Minio API
SPAIN_MINIO_API= # URL of the Spain Minio API

MINIO_REGION= # Region of the Minio server
MINIO_ACCESS_KEY_ID= # Access key of the Minio server
MINIO_ACCESS_KEY= # Secret key of the Minio server
```

### Run the application
```bash
cd workflow-data-replication-api
python3 run.py
```

# Kubernetes, docker and helm
First make sure minikube, docker and helm are installed on you system

```bash
minikube start --driver=docker

cd workflow-data-replication-api

docker compose build 

minikube image load lifewatch:latest

docker compose up
```

### Open a new tab to run a lokal kubernetes image with helm

```bash
cd workflow-data-replication-api
helm package lifewatch
helm install lifewatch ./lifewatch

# Get service URL
kubectl port-forward service/lifewatch-service 5000:80
```

### Access the Swagger UI
Open a browser and navigate to `http://localhost:5000`
The Swagger UI is available at the API root URL.

### Reset minikube:
```bash
minikube stop                       
minikube delete
minikube start --driver=docker
```