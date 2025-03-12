# Testing

### Check your enviroment
```bash
source venv/bin/activate
cd workflow-data-replication-api
pip install -r requirements.txt

```

### Install Pytest
```bash
pip install requests pytest
```

### Run Python API before testing!
```bash
python3 run.py
```

### Run tests
```bash
pytest test_api.py -v

OR

python -m unittest test_api.py
```
