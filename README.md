# RetailProject

Small PySpark project: reads `orders` and `customers`, keeps only **CLOSED** orders, joins them to
customers and counts closed orders per **state**.

```
RetailProject
├── configs/              # per-environment settings (LOCAL / QA / PROD)
│   ├── application.conf  #   input paths
│   └── pyspark.conf      #   Spark settings
├── data/                 # sample input (no header) + expected test output
├── lib/                  # ConfigReader, DataReader, DataManipulation, Utils
├── application_main.py   # job entry point
├── conftest.py           # shared pytest fixtures (SparkSession)
├── test_retail_proj.py   # unit tests
├── pytest.ini
├── Pipfile / requirements.txt
├── Jenkinsfile           # CI pipeline
└── log4j.properties      # Spark JVM logging
```

## Prerequisites
* Python 3.9+ (Pipfile asks for 3.11 - change `python_version` if you use another)
* Java 8 / 11 / 17 on your PATH (required by Spark): `java -version`

## Setup
```bash
# Option A - pipenv
pip install pipenv
pipenv install --dev        # also creates Pipfile.lock
pipenv shell

# Option B - plain venv
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the job
```bash
python application_main.py LOCAL
```

## Run the tests
```bash
pytest
```
In VS Code: open the folder, pick the interpreter (Ctrl/Cmd+Shift+P -> *Python: Select Interpreter*),
then use the Testing panel or the *Run application_main.py (LOCAL)* debug configuration.
