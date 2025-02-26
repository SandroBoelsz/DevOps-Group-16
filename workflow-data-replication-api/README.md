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

# Kubernetes and docker
```bash
minikube start --driver=docker

cd workflow-data-replication-api

docker compose build 

docker compose up
```

### Open a new tab to run a lokal kubernetes image

```bash
minikube image load workflow-api

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

minikube service workflow-api-service --url
```