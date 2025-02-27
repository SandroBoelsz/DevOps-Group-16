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

### Access the Swagger UI
Open a browser and navigate to `http://localhost:5000`
The Swagger UI is available at the API root URL.

