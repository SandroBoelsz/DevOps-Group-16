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

### Run the application
```bash
cd workflow-data-replication-api
python3 run.py
```

### Access the Swagger UI
Open a browser and navigate to `http://localhost:5000`
The Swagger UI is available at the API root URL.


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
minikube service lifewatch-service --url
```
