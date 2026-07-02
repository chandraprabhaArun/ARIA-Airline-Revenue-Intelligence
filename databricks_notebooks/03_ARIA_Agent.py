{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782504490745,
     "inputWidgets": {},
     "nuid": "6136d418-eacf-4dc9-80e9-a3e0f06aae98",
     "showTitle": false,
     "startTime": 1782504478882,
     "submitTime": 1782504478748,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: mlflow in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (3.14.0)\nRequirement already satisfied: mlflow-skinny==3.14.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (3.14.0)\nRequirement already satisfied: mlflow-tracing==3.14.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (3.14.0)\nRequirement already satisfied: Flask-CORS<7 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (6.0.5)\nRequirement already satisfied: Flask<4 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (2.2.5)\nRequirement already satisfied: aiohttp<4,>=3.7.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (3.8.5)\nRequirement already satisfied: alembic!=1.10.0,<2 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (1.18.5)\nRequirement already satisfied: cryptography<49,>=43.0.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (48.0.1)\nRequirement already satisfied: docker<8,>=4.0.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (7.1.0)\nRequirement already satisfied: graphene<4 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (3.4.3)\nRequirement already satisfied: gunicorn<27 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (20.1.0)\nRequirement already satisfied: huey<4,>=2.5.4 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (3.0.3)\nRequirement already satisfied: matplotlib<4 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (3.7.2)\nRequirement already satisfied: numpy<3 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (1.26.4)\nRequirement already satisfied: pandas<3 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (1.5.3)\nRequirement already satisfied: pyarrow<25,>=4.0.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (14.0.1)\nRequirement already satisfied: scikit-learn<2 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (1.3.0)\nRequirement already satisfied: scipy<2 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (1.11.1)\nRequirement already satisfied: skops<1 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow) (0.14.0)\nRequirement already satisfied: sqlalchemy<3,>=1.4.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow) (1.4.39)\nRequirement already satisfied: cachetools<8,>=5.0.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (5.4.0)\nRequirement already satisfied: click<9,>=7.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (8.0.4)\nRequirement already satisfied: cloudpickle<4 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (2.2.1)\nRequirement already satisfied: databricks-sdk<1,>=0.20.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (0.20.0)\nRequirement already satisfied: fastapi<1 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (0.138.1)\nRequirement already satisfied: gitpython<4,>=3.1.9 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (3.1.27)\nRequirement already satisfied: importlib_metadata!=4.7.0,<10,>=3.7.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (6.0.0)\nRequirement already satisfied: opentelemetry-api<3,>=1.9.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (1.25.0)\nRequirement already satisfied: opentelemetry-proto<3,>=1.9.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (1.43.0)\nRequirement already satisfied: opentelemetry-sdk<3,>=1.9.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (1.25.0)\nRequirement already satisfied: packaging<27 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (23.2)\nRequirement already satisfied: protobuf<8,>=3.12.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (7.35.1)\nRequirement already satisfied: pydantic<3,>=2.0.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (2.13.4)\nRequirement already satisfied: python-dotenv<2,>=0.19.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (1.2.2)\nRequirement already satisfied: pyyaml<7,>=5.1 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (6.0)\nRequirement already satisfied: requests<3,>=2.17.3 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (2.31.0)\nRequirement already satisfied: sqlparse<1,>=0.4.0 in /databricks/python3/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (0.4.2)\nRequirement already satisfied: starlette<2 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (1.3.1)\nRequirement already satisfied: typing-extensions<5,>=4.0.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (4.15.0)\nRequirement already satisfied: uvicorn<1 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from mlflow-skinny==3.14.0->mlflow) (0.49.0)\nRequirement already satisfied: attrs>=17.3.0 in /databricks/python3/lib/python3.11/site-packages (from aiohttp<4,>=3.7.0->mlflow) (22.1.0)\nRequirement already satisfied: charset-normalizer<4.0,>=2.0 in /databricks/python3/lib/python3.11/site-packages (from aiohttp<4,>=3.7.0->mlflow) (2.0.4)\nRequirement already satisfied: multidict<7.0,>=4.5 in /databricks/python3/lib/python3.11/site-packages (from aiohttp<4,>=3.7.0->mlflow) (6.0.2)\nRequirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /databricks/python3/lib/python3.11/site-packages (from aiohttp<4,>=3.7.0->mlflow) (4.0.2)\nRequirement already satisfied: yarl<2.0,>=1.0 in /databricks/python3/lib/python3.11/site-packages (from aiohttp<4,>=3.7.0->mlflow) (1.8.1)\nRequirement already satisfied: frozenlist>=1.1.1 in /databricks/python3/lib/python3.11/site-packages (from aiohttp<4,>=3.7.0->mlflow) (1.3.3)\nRequirement already satisfied: aiosignal>=1.1.2 in /databricks/python3/lib/python3.11/site-packages (from aiohttp<4,>=3.7.0->mlflow) (1.2.0)\nRequirement already satisfied: Mako in /databricks/python3/lib/python3.11/site-packages (from alembic!=1.10.0,<2->mlflow) (1.2.0)\nRequirement already satisfied: cffi>=2.0.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from cryptography<49,>=43.0.0->mlflow) (2.0.0)\nRequirement already satisfied: urllib3>=1.26.0 in /databricks/python3/lib/python3.11/site-packages (from docker<8,>=4.0.0->mlflow) (1.26.16)\nRequirement already satisfied: Werkzeug>=2.2.2 in /databricks/python3/lib/python3.11/site-packages (from Flask<4->mlflow) (2.2.3)\nRequirement already satisfied: Jinja2>=3.0 in /databricks/python3/lib/python3.11/site-packages (from Flask<4->mlflow) (3.1.2)\nRequirement already satisfied: itsdangerous>=2.0 in /databricks/python3/lib/python3.11/site-packages (from Flask<4->mlflow) (2.0.1)\nRequirement already satisfied: graphql-core<3.3,>=3.1 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from graphene<4->mlflow) (3.2.11)\nRequirement already satisfied: graphql-relay<3.3,>=3.1 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from graphene<4->mlflow) (3.2.0)\nRequirement already satisfied: python-dateutil<3,>=2.7.0 in /databricks/python3/lib/python3.11/site-packages (from graphene<4->mlflow) (2.8.2)\nRequirement already satisfied: setuptools>=3.0 in /databricks/python3/lib/python3.11/site-packages (from gunicorn<27->mlflow) (68.0.0)\nRequirement already satisfied: contourpy>=1.0.1 in /databricks/python3/lib/python3.11/site-packages (from matplotlib<4->mlflow) (1.0.5)\nRequirement already satisfied: cycler>=0.10 in /databricks/python3/lib/python3.11/site-packages (from matplotlib<4->mlflow) (0.11.0)\nRequirement already satisfied: fonttools>=4.22.0 in /databricks/python3/lib/python3.11/site-packages (from matplotlib<4->mlflow) (4.25.0)\nRequirement already satisfied: kiwisolver>=1.0.1 in /databricks/python3/lib/python3.11/site-packages (from matplotlib<4->mlflow) (1.4.4)\nRequirement already satisfied: pillow>=6.2.0 in /databricks/python3/lib/python3.11/site-packages (from matplotlib<4->mlflow) (9.4.0)\nRequirement already satisfied: pyparsing<3.1,>=2.3.1 in /databricks/python3/lib/python3.11/site-packages (from matplotlib<4->mlflow) (3.0.9)\nRequirement already satisfied: pytz>=2020.1 in /databricks/python3/lib/python3.11/site-packages (from pandas<3->mlflow) (2022.7)\nRequirement already satisfied: joblib>=1.1.1 in /databricks/python3/lib/python3.11/site-packages (from scikit-learn<2->mlflow) (1.2.0)\nRequirement already satisfied: threadpoolctl>=2.0.0 in /databricks/python3/lib/python3.11/site-packages (from scikit-learn<2->mlflow) (2.2.0)\nRequirement already satisfied: prettytable>=3.9 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from skops<1->mlflow) (3.18.0)\nRequirement already satisfied: greenlet!=0.4.17 in /databricks/python3/lib/python3.11/site-packages (from sqlalchemy<3,>=1.4.0->mlflow) (2.0.1)\nRequirement already satisfied: pycparser in /databricks/python3/lib/python3.11/site-packages (from cffi>=2.0.0->cryptography<49,>=43.0.0->mlflow) (2.21)\nRequirement already satisfied: google-auth~=2.0 in /databricks/python3/lib/python3.11/site-packages (from databricks-sdk<1,>=0.20.0->mlflow-skinny==3.14.0->mlflow) (2.21.0)\nRequirement already satisfied: typing-inspection>=0.4.2 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from fastapi<1->mlflow-skinny==3.14.0->mlflow) (0.4.2)\nRequirement already satisfied: annotated-doc>=0.0.2 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from fastapi<1->mlflow-skinny==3.14.0->mlflow) (0.0.4)\nRequirement already satisfied: gitdb<5,>=4.0.1 in /databricks/python3/lib/python3.11/site-packages (from gitpython<4,>=3.1.9->mlflow-skinny==3.14.0->mlflow) (4.0.11)\nRequirement already satisfied: zipp>=0.5 in /databricks/python3/lib/python3.11/site-packages (from importlib_metadata!=4.7.0,<10,>=3.7.0->mlflow-skinny==3.14.0->mlflow) (3.11.0)\nRequirement already satisfied: MarkupSafe>=2.0 in /databricks/python3/lib/python3.11/site-packages (from Jinja2>=3.0->Flask<4->mlflow) (2.1.1)\nRequirement already satisfied: deprecated>=1.2.6 in /databricks/python3/lib/python3.11/site-packages (from opentelemetry-api<3,>=1.9.0->mlflow-skinny==3.14.0->mlflow) (1.2.14)\nRequirement already satisfied: opentelemetry-semantic-conventions==0.46b0 in /databricks/python3/lib/python3.11/site-packages (from opentelemetry-sdk<3,>=1.9.0->mlflow-skinny==3.14.0->mlflow) (0.46b0)\nRequirement already satisfied: wcwidth>=0.3.5 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from prettytable>=3.9->skops<1->mlflow) (0.8.1)\nRequirement already satisfied: annotated-types>=0.6.0 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from pydantic<3,>=2.0.0->mlflow-skinny==3.14.0->mlflow) (0.7.0)\nRequirement already satisfied: pydantic-core==2.46.4 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from pydantic<3,>=2.0.0->mlflow-skinny==3.14.0->mlflow) (2.46.4)\nRequirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil<3,>=2.7.0->graphene<4->mlflow) (1.16.0)\nRequirement already satisfied: idna<4,>=2.5 in /databricks/python3/lib/python3.11/site-packages (from requests<3,>=2.17.3->mlflow-skinny==3.14.0->mlflow) (3.4)\nRequirement already satisfied: certifi>=2017.4.17 in /databricks/python3/lib/python3.11/site-packages (from requests<3,>=2.17.3->mlflow-skinny==3.14.0->mlflow) (2023.7.22)\nRequirement already satisfied: anyio<5,>=3.6.2 in /local_disk0/.ephemeral_nfs/envs/pythonEnv-d0ff849a-c572-4b00-a98d-1ab71464a342/lib/python3.11/site-packages (from starlette<2->mlflow-skinny==3.14.0->mlflow) (4.14.1)\nRequirement already satisfied: h11>=0.8 in /databricks/python3/lib/python3.11/site-packages (from uvicorn<1->mlflow-skinny==3.14.0->mlflow) (0.14.0)\nRequirement already satisfied: wrapt<2,>=1.10 in /databricks/python3/lib/python3.11/site-packages (from deprecated>=1.2.6->opentelemetry-api<3,>=1.9.0->mlflow-skinny==3.14.0->mlflow) (1.14.1)\nRequirement already satisfied: smmap<6,>=3.0.1 in /databricks/python3/lib/python3.11/site-packages (from gitdb<5,>=4.0.1->gitpython<4,>=3.1.9->mlflow-skinny==3.14.0->mlflow) (5.0.0)\nRequirement already satisfied: pyasn1-modules>=0.2.1 in /databricks/python3/lib/python3.11/site-packages (from google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.14.0->mlflow) (0.2.8)\nRequirement already satisfied: rsa<5,>=3.1.4 in /databricks/python3/lib/python3.11/site-packages (from google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.14.0->mlflow) (4.9)\nRequirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /databricks/python3/lib/python3.11/site-packages (from pyasn1-modules>=0.2.1->google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.14.0->mlflow) (0.4.8)\n\u001B[43mNote: you may need to restart the kernel using %restart_python or dbutils.library.restartPython() to use updated packages.\u001B[0m\n"
     ]
    }
   ],
   "source": [
    "%pip install -U mlflow\n",
    "dbutils.library.restartPython()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782504521285,
     "inputWidgets": {},
     "nuid": "4091c7dd-b05c-4204-aec6-426c84919f8b",
     "showTitle": false,
     "startTime": 1782504520645,
     "submitTime": 1782504520581,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/06/26 20:08:40 WARNING mlflow.utils.autologging_utils: MLflow openai autologging is known to be compatible with 1.87.0 <= openai, but the installed version is 1.35.3. If you encounter errors during autologging, try upgrading / downgrading openai to a compatible version, or try upgrading MLflow.\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MLflow ready!\n"
     ]
    }
   ],
   "source": [
    "import mlflow\n",
    "mlflow.openai.autolog()\n",
    "print(\"MLflow ready!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782504543410,
     "inputWidgets": {},
     "nuid": "e09deb39-6d5b-450d-86f5-c3354ac11766",
     "showTitle": false,
     "startTime": 1782504543015,
     "submitTime": 1782504542869,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total runs found: 0\nEmpty DataFrame\nColumns: [run_id, start_time, status]\nIndex: []\n"
     ]
    }
   ],
   "source": [
    "import mlflow\n",
    "\n",
    "runs = mlflow.search_runs(order_by=[\"start_time ASC\"])\n",
    "print(f\"Total runs found: {len(runs)}\")\n",
    "print(runs[['run_id', 'start_time', 'status']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782505094120,
     "inputWidgets": {},
     "nuid": "61154290-e2b1-47e6-9d06-e72708384954",
     "showTitle": false,
     "startTime": 1782505048198,
     "submitTime": 1782505048023,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading data from Delta Lake...\n✅ Loaded 500,000 records\n✅ Airlines encoded: ['EK' 'EY' 'FZ' 'G9' 'WY']\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001B[1;38;5;208mIf you are using MLflow Tracing, you can migrate your traces to Unity Catalog for unlimited storage, fine-grained access controls, and queryability from notebooks, SQL, and dashboards. \u001B[94mLearn more: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-traces-to-uc\u001B[0m\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\nTraining Model 1: Demand Forecasting...\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/06/26 20:17:33 WARNING mlflow.models.model: `artifact_path` is deprecated. Please use `name` instead.\n\uD83D\uDD17 View Logged Model at: https://adb-7405607151403283.3.azuredatabricks.net/ml/experiments/450047789329140/models/m-8d149c56ccdb441bbe0e1b84e4345fa5?o=7405607151403283\n2026/06/26 20:17:44 INFO mlflow.models.model: Model logged without a signature. Signatures are required for Databricks UC model registry as they validate model inputs and denote the expected schema of model outputs. Please set `input_example` parameter when logging the model to auto infer the model signature. To manually set the signature, please visit https://www.mlflow.org/docs/3.14.0/ml/model/signatures.html for instructions on setting signature on models.\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Demand Model | R2: 0.8852 | Accuracy: 87.8%\n   Run ID: 4f9ad1d9916041b38ea51e7e17372a71\n\nTraining Model 2: Dynamic Pricing...\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/06/26 20:17:48 WARNING mlflow.models.model: `artifact_path` is deprecated. Please use `name` instead.\n\uD83D\uDD17 View Logged Model at: https://adb-7405607151403283.3.azuredatabricks.net/ml/experiments/450047789329140/models/m-bdd314809a6c46cfb49b89b2f6ebbe4a?o=7405607151403283\n2026/06/26 20:17:58 INFO mlflow.models.model: Model logged without a signature. Signatures are required for Databricks UC model registry as they validate model inputs and denote the expected schema of model outputs. Please set `input_example` parameter when logging the model to auto infer the model signature. To manually set the signature, please visit https://www.mlflow.org/docs/3.14.0/ml/model/signatures.html for instructions on setting signature on models.\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Pricing Model | R2: 0.9969 | Accuracy: 97.5%\n   Run ID: 089cd19a2049449eb2b93b8b44f57c08\n\nTraining Model 3: Revenue Optimization...\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/06/26 20:18:03 WARNING mlflow.models.model: `artifact_path` is deprecated. Please use `name` instead.\n\uD83D\uDD17 View Logged Model at: https://adb-7405607151403283.3.azuredatabricks.net/ml/experiments/450047789329140/models/m-6b1c3ebe66ae4bf080102b83c6e2c77f?o=7405607151403283\n2026/06/26 20:18:12 INFO mlflow.models.model: Model logged without a signature. Signatures are required for Databricks UC model registry as they validate model inputs and denote the expected schema of model outputs. Please set `input_example` parameter when logging the model to auto infer the model signature. To manually set the signature, please visit https://www.mlflow.org/docs/3.14.0/ml/model/signatures.html for instructions on setting signature on models.\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Revenue Model | R2: 0.9999 | Accuracy: 99.5%\n   Run ID: b5146e7c0295485e8284e93e510dec9b\n\n=======================================================\nALL 3 MODELS TRAINED AND SAVED TO MLFLOW!\n=======================================================\ndemand_run_id  = '4f9ad1d9916041b38ea51e7e17372a71'\npricing_run_id = '089cd19a2049449eb2b93b8b44f57c08'\nrevenue_run_id = 'b5146e7c0295485e8284e93e510dec9b'\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import mlflow\n",
    "import mlflow.sklearn\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n",
    "from xgboost import XGBRegressor\n",
    "\n",
    "# Load data from Delta table\n",
    "print(\"Loading data from Delta Lake...\")\n",
    "df = spark.sql(\"SELECT * FROM aria_flights\").toPandas()\n",
    "print(f\"✅ Loaded {len(df):,} records\")\n",
    "\n",
    "le = LabelEncoder()\n",
    "df['AIRLINE_ENC'] = le.fit_transform(df['AIRLINE'])\n",
    "print(f\"✅ Airlines encoded: {le.classes_}\")\n",
    "\n",
    "# ✅ FIX: Define trusted types for XGBoost\n",
    "TRUSTED_TYPES = [\"xgboost.core.Booster\", \"xgboost.sklearn.XGBRegressor\"]\n",
    "\n",
    "mlflow.set_experiment(\"/ARIA-Experiment\")\n",
    "\n",
    "# ============================================================\n",
    "# MODEL 1: Demand Forecasting\n",
    "# ============================================================\n",
    "print(\"\\nTraining Model 1: Demand Forecasting...\")\n",
    "\n",
    "DEMAND_FEATURES = ['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR',\n",
    "                   'IS_PEAK_HOUR','DISTANCE','TICKET_PRICE',\n",
    "                   'SEATS_CAPACITY','AIRLINE_ENC']\n",
    "\n",
    "X_d = df[DEMAND_FEATURES]\n",
    "y_d = df['SEATS_SOLD']\n",
    "X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(\n",
    "    X_d, y_d, test_size=0.2, random_state=42)\n",
    "\n",
    "with mlflow.start_run(run_name=\"demand_model\") as run_d:\n",
    "    model_demand = XGBRegressor(\n",
    "        n_estimators=100, max_depth=6,\n",
    "        learning_rate=0.1, random_state=42, verbosity=0)\n",
    "    model_demand.fit(X_train_d, y_train_d)\n",
    "    y_pred_d = model_demand.predict(X_test_d)\n",
    "    mape_d = np.mean(np.abs((y_test_d - y_pred_d) / y_test_d)) * 100\n",
    "    r2_d   = r2_score(y_test_d, y_pred_d)\n",
    "    mlflow.log_metric(\"MAPE\", mape_d)\n",
    "    mlflow.log_metric(\"R2\",   r2_d)\n",
    "    # ✅ KEY FIX: pass skops_trusted_types\n",
    "    mlflow.sklearn.log_model(\n",
    "        model_demand, \"demand_model\",\n",
    "        skops_trusted_types=TRUSTED_TYPES)\n",
    "    demand_run_id = run_d.info.run_id\n",
    "\n",
    "print(f\"✅ Demand Model | R2: {r2_d:.4f} | Accuracy: {100-mape_d:.1f}%\")\n",
    "print(f\"   Run ID: {demand_run_id}\")\n",
    "\n",
    "# ============================================================\n",
    "# MODEL 2: Dynamic Pricing\n",
    "# ============================================================\n",
    "print(\"\\nTraining Model 2: Dynamic Pricing...\")\n",
    "\n",
    "PRICING_FEATURES = ['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR',\n",
    "                    'IS_PEAK_HOUR','DISTANCE','LOAD_FACTOR',\n",
    "                    'SEATS_CAPACITY','AIRLINE_ENC']\n",
    "\n",
    "X_p = df[PRICING_FEATURES]\n",
    "y_p = df['TICKET_PRICE']\n",
    "X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(\n",
    "    X_p, y_p, test_size=0.2, random_state=42)\n",
    "\n",
    "with mlflow.start_run(run_name=\"pricing_model\") as run_p:\n",
    "    model_pricing = XGBRegressor(\n",
    "        n_estimators=100, max_depth=6,\n",
    "        learning_rate=0.1, random_state=42, verbosity=0)\n",
    "    model_pricing.fit(X_train_p, y_train_p)\n",
    "    y_pred_p = model_pricing.predict(X_test_p)\n",
    "    mape_p = np.mean(np.abs((y_test_p - y_pred_p) / y_test_p)) * 100\n",
    "    r2_p   = r2_score(y_test_p, y_pred_p)\n",
    "    mlflow.log_metric(\"MAPE\", mape_p)\n",
    "    mlflow.log_metric(\"R2\",   r2_p)\n",
    "    mlflow.sklearn.log_model(\n",
    "        model_pricing, \"pricing_model\",\n",
    "        skops_trusted_types=TRUSTED_TYPES)\n",
    "    pricing_run_id = run_p.info.run_id\n",
    "\n",
    "print(f\"✅ Pricing Model | R2: {r2_p:.4f} | Accuracy: {100-mape_p:.1f}%\")\n",
    "print(f\"   Run ID: {pricing_run_id}\")\n",
    "\n",
    "# ============================================================\n",
    "# MODEL 3: Revenue Optimization\n",
    "# ============================================================\n",
    "print(\"\\nTraining Model 3: Revenue Optimization...\")\n",
    "\n",
    "REVENUE_FEATURES = ['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR',\n",
    "                    'IS_PEAK_HOUR','DISTANCE','LOAD_FACTOR',\n",
    "                    'SEATS_CAPACITY','SEATS_SOLD','TICKET_PRICE','AIRLINE_ENC']\n",
    "\n",
    "X_r = df[REVENUE_FEATURES]\n",
    "y_r = df['FLIGHT_REVENUE']\n",
    "X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(\n",
    "    X_r, y_r, test_size=0.2, random_state=42)\n",
    "\n",
    "with mlflow.start_run(run_name=\"revenue_model\") as run_r:\n",
    "    model_revenue = XGBRegressor(\n",
    "        n_estimators=150, max_depth=7,\n",
    "        learning_rate=0.08, random_state=42, verbosity=0)\n",
    "    model_revenue.fit(X_train_r, y_train_r)\n",
    "    y_pred_r = model_revenue.predict(X_test_r)\n",
    "    mape_r = np.mean(np.abs((y_test_r - y_pred_r) / y_test_r)) * 100\n",
    "    r2_r   = r2_score(y_test_r, y_pred_r)\n",
    "    mlflow.log_metric(\"MAPE\", mape_r)\n",
    "    mlflow.log_metric(\"R2\",   r2_r)\n",
    "    mlflow.sklearn.log_model(\n",
    "        model_revenue, \"revenue_model\",\n",
    "        skops_trusted_types=TRUSTED_TYPES)\n",
    "    revenue_run_id = run_r.info.run_id\n",
    "\n",
    "print(f\"✅ Revenue Model | R2: {r2_r:.4f} | Accuracy: {100-mape_r:.1f}%\")\n",
    "print(f\"   Run ID: {revenue_run_id}\")\n",
    "\n",
    "print(\"\\n\" + \"=\"*55)\n",
    "print(\"ALL 3 MODELS TRAINED AND SAVED TO MLFLOW!\")\n",
    "print(\"=\"*55)\n",
    "print(f\"demand_run_id  = '{demand_run_id}'\")\n",
    "print(f\"pricing_run_id = '{pricing_run_id}'\")\n",
    "print(f\"revenue_run_id = '{revenue_run_id}'\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782505511699,
     "inputWidgets": {},
     "nuid": "3870c806-b40a-4166-981d-7be75a72287b",
     "showTitle": true,
     "startTime": 1782505504519,
     "submitTime": 1782505504476,
     "tableResultSettingsMap": {},
     "title": "Load Models:"
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b27939466d1d4e08bf54c19e4ef6bcc7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading artifacts:   0%|          | 0/1 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "507191fbe8554503b30031d0a4646221",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading artifacts:   0%|          | 0/9 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bf7a2de4ad9f434d851503d84315587c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading artifacts:   0%|          | 0/1 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "76589a8d5aad49c5be1a1b16639b8a1e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading artifacts:   0%|          | 0/9 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c935f157190e42a9a934f85447afa1a7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading artifacts:   0%|          | 0/1 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "57fc6a54dfd14855937269aa31bccc0f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading artifacts:   0%|          | 0/9 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ All 3 models loaded!\n✅ OpenAI client ready!\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 3: Load all 3 trained models\n",
    "# ============================================================\n",
    "\n",
    "import mlflow.sklearn\n",
    "from openai import OpenAI\n",
    "import json\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "# Load models using run IDs captured above\n",
    "model_demand  = mlflow.sklearn.load_model(f\"runs:/{demand_run_id}/demand_model\")\n",
    "model_pricing = mlflow.sklearn.load_model(f\"runs:/{pricing_run_id}/pricing_model\")\n",
    "model_revenue = mlflow.sklearn.load_model(f\"runs:/{revenue_run_id}/revenue_model\")\n",
    "\n",
    "# OpenAI client\n",
    "client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))\n",
    "\n",
    "# Label encoder\n",
    "le = LabelEncoder()\n",
    "le.classes_ = np.array([\"EK\", \"EY\", \"FZ\", \"G9\", \"WY\"])\n",
    "\n",
    "print(\"✅ All 3 models loaded!\")\n",
    "print(\"✅ OpenAI client ready!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782505623621,
     "inputWidgets": {},
     "nuid": "31b39697-b028-491e-a68e-61eef0053151",
     "showTitle": true,
     "startTime": 1782505623464,
     "submitTime": 1782505623335,
     "tableResultSettingsMap": {},
     "title": "Define Agent Tools:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ All 3 agent tools defined!\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 4: Define the 3 specialized agent tools\n",
    "# ============================================================\n",
    "\n",
    "def forecast_demand(route, month, day_of_week, is_weekend,\n",
    "                    dep_hour, distance, ticket_price,\n",
    "                    seats_capacity, airline):\n",
    "    \"\"\"AGENT 1: Predicts how many seats will be sold\"\"\"\n",
    "    airline_enc  = list(le.classes_).index(airline) if airline in le.classes_ else 0\n",
    "    is_peak_hour = 1 if (7 <= dep_hour <= 9) or (17 <= dep_hour <= 19) else 0\n",
    "\n",
    "    features = pd.DataFrame([[\n",
    "        month, day_of_week, is_weekend, dep_hour,\n",
    "        is_peak_hour, distance, ticket_price,\n",
    "        seats_capacity, airline_enc\n",
    "    ]], columns=[\n",
    "        'MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR',\n",
    "        'IS_PEAK_HOUR','DISTANCE','TICKET_PRICE',\n",
    "        'SEATS_CAPACITY','AIRLINE_ENC'\n",
    "    ])\n",
    "\n",
    "    predicted_seats = int(model_demand.predict(features)[0])\n",
    "    load_factor     = round(predicted_seats / seats_capacity, 3)\n",
    "\n",
    "    result = {\n",
    "        \"predicted_seats_sold\": predicted_seats,\n",
    "        \"load_factor\":          load_factor,\n",
    "        \"demand_level\":         \"HIGH\" if load_factor > 0.85 else \"MEDIUM\" if load_factor > 0.65 else \"LOW\"\n",
    "    }\n",
    "    print(f\"  ✈️  Demand Agent Result: {result}\")\n",
    "    return result\n",
    "\n",
    "\n",
    "def recommend_price(month, day_of_week, is_weekend, dep_hour,\n",
    "                    distance, load_factor, seats_capacity, airline):\n",
    "    \"\"\"AGENT 2: Recommends optimal ticket price\"\"\"\n",
    "    airline_enc  = list(le.classes_).index(airline) if airline in le.classes_ else 0\n",
    "    is_peak_hour = 1 if (7 <= dep_hour <= 9) or (17 <= dep_hour <= 19) else 0\n",
    "\n",
    "    features = pd.DataFrame([[\n",
    "        month, day_of_week, is_weekend, dep_hour,\n",
    "        is_peak_hour, distance, load_factor,\n",
    "        seats_capacity, airline_enc\n",
    "    ]], columns=[\n",
    "        'MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR',\n",
    "        'IS_PEAK_HOUR','DISTANCE','LOAD_FACTOR',\n",
    "        'SEATS_CAPACITY','AIRLINE_ENC'\n",
    "    ])\n",
    "\n",
    "    price = round(float(model_pricing.predict(features)[0]), 2)\n",
    "\n",
    "    result = {\n",
    "        \"recommended_price\":  price,\n",
    "        \"pricing_strategy\":   \"PREMIUM\" if price > 500 else \"STANDARD\" if price > 250 else \"BUDGET\"\n",
    "    }\n",
    "    print(f\"  \uD83D\uDCB0 Pricing Agent Result: {result}\")\n",
    "    return result\n",
    "\n",
    "\n",
    "def optimize_revenue(month, day_of_week, is_weekend, dep_hour,\n",
    "                     distance, load_factor, seats_capacity,\n",
    "                     seats_sold, ticket_price, airline):\n",
    "    \"\"\"AGENT 3: Predicts total flight revenue\"\"\"\n",
    "    airline_enc  = list(le.classes_).index(airline) if airline in le.classes_ else 0\n",
    "    is_peak_hour = 1 if (7 <= dep_hour <= 9) or (17 <= dep_hour <= 19) else 0\n",
    "\n",
    "    features = pd.DataFrame([[\n",
    "        month, day_of_week, is_weekend, dep_hour,\n",
    "        is_peak_hour, distance, load_factor,\n",
    "        seats_capacity, seats_sold, ticket_price, airline_enc\n",
    "    ]], columns=[\n",
    "        'MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR',\n",
    "        'IS_PEAK_HOUR','DISTANCE','LOAD_FACTOR',\n",
    "        'SEATS_CAPACITY','SEATS_SOLD','TICKET_PRICE','AIRLINE_ENC'\n",
    "    ])\n",
    "\n",
    "    predicted_revenue = round(float(model_revenue.predict(features)[0]), 2)\n",
    "    max_possible      = seats_capacity * ticket_price\n",
    "    efficiency        = round(predicted_revenue / max_possible * 100, 1)\n",
    "\n",
    "    result = {\n",
    "        \"predicted_revenue\":    predicted_revenue,\n",
    "        \"max_possible_revenue\": round(max_possible, 2),\n",
    "        \"revenue_efficiency\":   f\"{efficiency}%\",\n",
    "        \"recommendation\":       \"INCREASE PRICE\" if efficiency < 70 else \"MAINTAIN\" if efficiency < 90 else \"OPTIMAL\"\n",
    "    }\n",
    "    print(f\"  \uD83D\uDCC8 Revenue Agent Result: {result}\")\n",
    "    return result\n",
    "\n",
    "print(\"✅ All 3 agent tools defined!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782505629227,
     "inputWidgets": {},
     "nuid": "0e99bb23-02de-4d8f-b901-852b5ee78d7a",
     "showTitle": true,
     "startTime": 1782505629101,
     "submitTime": 1782505629051,
     "tableResultSettingsMap": {},
     "title": "The Orchestrator (The Brain):"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ ARIA Orchestrator ready!\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 5: ARIA Orchestrator Agent\n",
    "# ============================================================\n",
    "\n",
    "tools = [\n",
    "    {\n",
    "        \"type\": \"function\",\n",
    "        \"function\": {\n",
    "            \"name\": \"forecast_demand\",\n",
    "            \"description\": \"Predicts seat demand. Always call this FIRST.\",\n",
    "            \"parameters\": {\n",
    "                \"type\": \"object\",\n",
    "                \"properties\": {\n",
    "                    \"route\":          {\"type\": \"string\"},\n",
    "                    \"month\":          {\"type\": \"integer\"},\n",
    "                    \"day_of_week\":    {\"type\": \"integer\"},\n",
    "                    \"is_weekend\":     {\"type\": \"integer\"},\n",
    "                    \"dep_hour\":       {\"type\": \"integer\"},\n",
    "                    \"distance\":       {\"type\": \"integer\"},\n",
    "                    \"ticket_price\":   {\"type\": \"number\"},\n",
    "                    \"seats_capacity\": {\"type\": \"integer\"},\n",
    "                    \"airline\":        {\"type\": \"string\"}\n",
    "                },\n",
    "                \"required\": [\"route\",\"month\",\"day_of_week\",\"is_weekend\",\n",
    "                             \"dep_hour\",\"distance\",\"ticket_price\",\"seats_capacity\",\"airline\"]\n",
    "            }\n",
    "        }\n",
    "    },\n",
    "    {\n",
    "        \"type\": \"function\",\n",
    "        \"function\": {\n",
    "            \"name\": \"recommend_price\",\n",
    "            \"description\": \"Recommends optimal price. Call AFTER forecast_demand.\",\n",
    "            \"parameters\": {\n",
    "                \"type\": \"object\",\n",
    "                \"properties\": {\n",
    "                    \"month\":          {\"type\": \"integer\"},\n",
    "                    \"day_of_week\":    {\"type\": \"integer\"},\n",
    "                    \"is_weekend\":     {\"type\": \"integer\"},\n",
    "                    \"dep_hour\":       {\"type\": \"integer\"},\n",
    "                    \"distance\":       {\"type\": \"integer\"},\n",
    "                    \"load_factor\":    {\"type\": \"number\"},\n",
    "                    \"seats_capacity\": {\"type\": \"integer\"},\n",
    "                    \"airline\":        {\"type\": \"string\"}\n",
    "                },\n",
    "                \"required\": [\"month\",\"day_of_week\",\"is_weekend\",\"dep_hour\",\n",
    "                             \"distance\",\"load_factor\",\"seats_capacity\",\"airline\"]\n",
    "            }\n",
    "        }\n",
    "    },\n",
    "    {\n",
    "        \"type\": \"function\",\n",
    "        \"function\": {\n",
    "            \"name\": \"optimize_revenue\",\n",
    "            \"description\": \"Optimizes total revenue. Call LAST.\",\n",
    "            \"parameters\": {\n",
    "                \"type\": \"object\",\n",
    "                \"properties\": {\n",
    "                    \"month\":          {\"type\": \"integer\"},\n",
    "                    \"day_of_week\":    {\"type\": \"integer\"},\n",
    "                    \"is_weekend\":     {\"type\": \"integer\"},\n",
    "                    \"dep_hour\":       {\"type\": \"integer\"},\n",
    "                    \"distance\":       {\"type\": \"integer\"},\n",
    "                    \"load_factor\":    {\"type\": \"number\"},\n",
    "                    \"seats_capacity\": {\"type\": \"integer\"},\n",
    "                    \"seats_sold\":     {\"type\": \"integer\"},\n",
    "                    \"ticket_price\":   {\"type\": \"number\"},\n",
    "                    \"airline\":        {\"type\": \"string\"}\n",
    "                },\n",
    "                \"required\": [\"month\",\"day_of_week\",\"is_weekend\",\"dep_hour\",\"distance\",\n",
    "                             \"load_factor\",\"seats_capacity\",\"seats_sold\",\"ticket_price\",\"airline\"]\n",
    "            }\n",
    "        }\n",
    "    }\n",
    "]\n",
    "\n",
    "available_tools = {\n",
    "    \"forecast_demand\":  forecast_demand,\n",
    "    \"recommend_price\":  recommend_price,\n",
    "    \"optimize_revenue\": optimize_revenue\n",
    "}\n",
    "\n",
    "def run_aria_agent(flight_query):\n",
    "    print(\"\\n\" + \"=\"*60)\n",
    "    print(\"\uD83E\uDD16 ARIA AGENT ACTIVATED\")\n",
    "    print(\"=\"*60)\n",
    "    print(f\"Query: {flight_query}\")\n",
    "    print(\"-\"*60)\n",
    "\n",
    "    messages = [\n",
    "        {\n",
    "            \"role\": \"system\",\n",
    "            \"content\": \"\"\"You are ARIA, an Airline Revenue Intelligence Agent.\n",
    "            For every flight query you MUST:\n",
    "            1. Call forecast_demand first\n",
    "            2. Call recommend_price using load_factor from step 1\n",
    "            3. Call optimize_revenue with all data from steps 1 and 2\n",
    "            4. Give a clear business summary with specific numbers.\"\"\"\n",
    "        },\n",
    "        {\"role\": \"user\", \"content\": flight_query}\n",
    "    ]\n",
    "\n",
    "    step = 1\n",
    "    while True:\n",
    "        response = client.chat.completions.create(\n",
    "            model=\"gpt-4o-mini\",\n",
    "            messages=messages,\n",
    "            tools=tools,\n",
    "            tool_choice=\"auto\"\n",
    "        )\n",
    "\n",
    "        msg = response.choices[0].message\n",
    "\n",
    "        if msg.tool_calls:\n",
    "            messages.append(msg)\n",
    "            for tool_call in msg.tool_calls:\n",
    "                tool_name = tool_call.function.name\n",
    "                tool_args = json.loads(tool_call.function.arguments)\n",
    "                print(f\"\\n  Step {step}: Calling → {tool_name}()\")\n",
    "                step += 1\n",
    "                tool_result = available_tools[tool_name](**tool_args)\n",
    "                messages.append({\n",
    "                    \"role\":        \"tool\",\n",
    "                    \"tool_call_id\": tool_call.id,\n",
    "                    \"content\":     json.dumps(tool_result)\n",
    "                })\n",
    "        else:\n",
    "            print(\"\\n\" + \"=\"*60)\n",
    "            print(\"\uD83D\uDCCB ARIA FINAL RECOMMENDATION:\")\n",
    "            print(\"=\"*60)\n",
    "            print(msg.content)\n",
    "            print(\"=\"*60)\n",
    "            return msg.content\n",
    "\n",
    "print(\"✅ ARIA Orchestrator ready!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782505648994,
     "inputWidgets": {},
     "nuid": "ddf1a955-7aed-4f71-9443-919cd26d3808",
     "showTitle": true,
     "startTime": 1782505635592,
     "submitTime": 1782505635544,
     "tableResultSettingsMap": {},
     "title": "Run The Agent"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n============================================================\n\uD83E\uDD16 ARIA AGENT ACTIVATED\n============================================================\nQuery: \n    Analyze this flight and give revenue recommendations:\n    Route: DXB-LHR (Dubai to London)\n    Airline: EK (Emirates)\n    Month: December (month=12, peak holiday season)\n    Day: Friday (day_of_week=4, is_weekend=1)\n    Departure: 8:00 AM (dep_hour=8, peak hour)\n    Distance: 3400 miles\n    Aircraft capacity: 350 seats\n    Current ticket price: $450\n\n------------------------------------------------------------\n\n  Step 1: Calling → forecast_demand()\n  ✈️  Demand Agent Result: {'predicted_seats_sold': 236, 'load_factor': 0.674, 'demand_level': 'MEDIUM'}\n\n  Step 2: Calling → recommend_price()\n  \uD83D\uDCB0 Pricing Agent Result: {'recommended_price': 589.43, 'pricing_strategy': 'PREMIUM'}\n\n  Step 3: Calling → optimize_revenue()\n  \uD83D\uDCC8 Revenue Agent Result: {'predicted_revenue': 140191.69, 'max_possible_revenue': 206300.5, 'revenue_efficiency': '68.0%', 'recommendation': 'INCREASE PRICE'}\n\n============================================================\n\uD83D\uDCCB ARIA FINAL RECOMMENDATION:\n============================================================\n### Business Summary for Flight DXB-LHR (Emirates)\n\n- **Route:** Dubai to London (DXB-LHR)\n- **Date:** December (holiday peak season), Friday (Day 4 of the week)\n- **Departure Time:** 8:00 AM (Peak hour)\n- **Distance:** 3400 miles\n- **Aircraft Capacity:** 350 seats\n- **Current Ticket Price:** $450\n\n#### Demand Forecast:\n- **Predicted Seats Sold:** 236\n- **Load Factor:** 67.4%\n- **Demand Level:** Medium\n\n#### Pricing Recommendation:\n- **Recommended Ticket Price:** $589.43\n- **Pricing Strategy:** Premium\n\n#### Revenue Optimization:\n- **Predicted Revenue at Recommended Price:** $140,191.69\n- **Maximum Possible Revenue:** $206,300.50\n- **Revenue Efficiency:** 68.0%\n\n### Recommendation:\n- **Action:** Increase the ticket price to $589.43 to maximize revenue opportunities during the busy holiday season. The recommended pricing strategy takes into account the medium demand level while optimizing for higher yields. \n\nThis strategic increase in price along with the current load factor can enhance overall revenue performance for the flight.\n============================================================\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "application/databricks.mlflow.trace": "[{\"trace_id\": \"tr-624a9910168dedde455b385325bd5abf\", \"sql_warehouse_id\": null}, {\"trace_id\": \"tr-f9856aa76a07d9e1c6f0ceea90048bb0\", \"sql_warehouse_id\": null}, {\"trace_id\": \"tr-96d1f5db3950e203b3a288347381217b\", \"sql_warehouse_id\": null}, {\"trace_id\": \"tr-8e92a776030379e4bde4b1264024bc45\", \"sql_warehouse_id\": null}]",
      "text/plain": [
       "[Trace(trace_id=tr-624a9910168dedde455b385325bd5abf), Trace(trace_id=tr-f9856aa76a07d9e1c6f0ceea90048bb0), Trace(trace_id=tr-96d1f5db3950e203b3a288347381217b), Trace(trace_id=tr-8e92a776030379e4bde4b1264024bc45)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 6: RUN ARIA - Watch it think autonomously!\n",
    "# ============================================================\n",
    "\n",
    "result = run_aria_agent(\"\"\"\n",
    "    Analyze this flight and give revenue recommendations:\n",
    "    Route: DXB-LHR (Dubai to London)\n",
    "    Airline: EK (Emirates)\n",
    "    Month: December (month=12, peak holiday season)\n",
    "    Day: Friday (day_of_week=4, is_weekend=1)\n",
    "    Departure: 8:00 AM (dep_hour=8, peak hour)\n",
    "    Distance: 3400 miles\n",
    "    Aircraft capacity: 350 seats\n",
    "    Current ticket price: $450\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1782506447061,
     "inputWidgets": {},
     "nuid": "d68f001f-4ac7-4448-b954-a39c7fc159c2",
     "showTitle": false,
     "startTime": 1782506446920,
     "submitTime": 1782506446774,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "### Business Summary for Flight DXB-LHR (Emirates)\n\n- **Route:** Dubai to London (DXB-LHR)\n- **Date:** December (holiday peak season), Friday (Day 4 of the week)\n- **Departure Time:** 8:00 AM (Peak hour)\n- **Distance:** 3400 miles\n- **Aircraft Capacity:** 350 seats\n- **Current Ticket Price:** $450\n\n#### Demand Forecast:\n- **Predicted Seats Sold:** 236\n- **Load Factor:** 67.4%\n- **Demand Level:** Medium\n\n#### Pricing Recommendation:\n- **Recommended Ticket Price:** $589.43\n- **Pricing Strategy:** Premium\n\n#### Revenue Optimization:\n- **Predicted Revenue at Recommended Price:** $140,191.69\n- **Maximum Possible Revenue:** $206,300.50\n- **Revenue Efficiency:** 68.0%\n\n### Recommendation:\n- **Action:** Increase the ticket price to $589.43 to maximize revenue opportunities during the busy holiday season. The recommended pricing strategy takes into account the medium demand level while optimizing for higher yields. \n\nThis strategic increase in price along with the current load factor can enhance overall revenue performance for the flight.\n"
     ]
    }
   ],
   "source": [
    "# Check if Step 3 completed\n",
    "print(result)"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "5"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "experimentId": "450047789329140",
    "pythonIndentUnit": 4
   },
   "notebookName": "03_ARIA_Agent",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}