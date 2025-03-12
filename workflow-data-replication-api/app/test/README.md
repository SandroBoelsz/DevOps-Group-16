# Testing

### Check your enviroment
```bash
source venv/bin/activate
cd workflow-data-replication-api
pip install -r requirements.txt
python3 run.py
```

### Install Pytest
```bash
pip install requests pytest
```

### Run tests
```bash
pytest test_api.py -v

OR

python -m unittest test_api.py
```
