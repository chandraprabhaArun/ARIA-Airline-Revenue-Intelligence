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
     "finishTime": 1782501847151,
     "inputWidgets": {},
     "nuid": "43d1ae53-8c5f-49be-be96-1a07aedf7c47",
     "showTitle": false,
     "startTime": 1782501816420,
     "submitTime": 1782501798554,
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
      "\u001B[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\npetastorm 0.12.1 requires pyspark>=2.1.0, which is not installed.\ndatabricks-feature-engineering 0.8.0 requires mlflow-skinny[databricks]<3,>=2.11.0, but you have mlflow-skinny 3.14.0 which is incompatible.\ndatabricks-feature-engineering 0.8.0 requires protobuf<5,>=3.12.0, but you have protobuf 7.35.1 which is incompatible.\ngoogle-api-core 2.18.0 requires protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0.dev0,>=3.19.5, but you have protobuf 7.35.1 which is incompatible.\ngoogleapis-common-protos 1.63.0 requires protobuf!=3.20.0,!=3.20.1,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0.dev0,>=3.19.5, but you have protobuf 7.35.1 which is incompatible.\njupyter-server 1.23.4 requires anyio<4,>=3.1.0, but you have anyio 4.14.1 which is incompatible.\nmsal 1.29.0 requires cryptography<45,>=2.5, but you have cryptography 48.0.1 which is incompatible.\nnumba 0.57.1 requires numpy<1.25,>=1.21, but you have numpy 1.26.4 which is incompatible.\noci 2.126.4 requires cryptography<43.0.0,>=3.2.1, but you have cryptography 48.0.1 which is incompatible.\nproto-plus 1.24.0 requires protobuf<6.0.0dev,>=3.19.0, but you have protobuf 7.35.1 which is incompatible.\npyopenssl 23.2.0 requires cryptography!=40.0.0,!=40.0.1,<42,>=38.0.0, but you have cryptography 48.0.1 which is incompatible.\ntensorboard-plugin-profile 2.15.1 requires protobuf<5.0.0dev,>=3.19.6, but you have protobuf 7.35.1 which is incompatible.\ntensorflow 2.16.1 requires protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3, but you have protobuf 7.35.1 which is incompatible.\nydata-profiling 4.5.1 requires numpy<1.24,>=1.16.0, but you have numpy 1.26.4 which is incompatible.\nydata-profiling 4.5.1 requires pydantic<2,>=1.8.1, but you have pydantic 2.13.4 which is incompatible.\u001B[0m\u001B[31m\n\u001B[0m\u001B[43mNote: you may need to restart the kernel using %restart_python or dbutils.library.restartPython() to use updated packages.\u001B[0m\n"
     ]
    }
   ],
   "source": [
    "%pip install mlflow xgboost scikit-learn --quiet"
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
     "finishTime": 1782501909900,
     "inputWidgets": {},
     "nuid": "26c6bca6-18cd-499c-9da0-d0f4bd67450f",
     "showTitle": true,
     "startTime": 1782501880673,
     "submitTime": 1782501880524,
     "tableResultSettingsMap": {},
     "title": "Load Data from Delta Table:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading data from Delta Lake table...\nLoaded 500,000 records\nColumns: ['FL_DATE', 'MONTH', 'DAY_OF_WEEK', 'IS_WEEKEND', 'AIRLINE', 'ORIGIN', 'DEST', 'ROUTE', 'DEP_HOUR', 'IS_PEAK_HOUR', 'DISTANCE', 'DEP_DELAY', 'SEATS_CAPACITY', 'SEATS_SOLD', 'LOAD_FACTOR', 'TICKET_PRICE', 'FLIGHT_REVENUE', 'DELAY_CATEGORY']\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FL_DATE</th>\n",
       "      <th>MONTH</th>\n",
       "      <th>DAY_OF_WEEK</th>\n",
       "      <th>IS_WEEKEND</th>\n",
       "      <th>AIRLINE</th>\n",
       "      <th>ORIGIN</th>\n",
       "      <th>DEST</th>\n",
       "      <th>ROUTE</th>\n",
       "      <th>DEP_HOUR</th>\n",
       "      <th>IS_PEAK_HOUR</th>\n",
       "      <th>DISTANCE</th>\n",
       "      <th>DEP_DELAY</th>\n",
       "      <th>SEATS_CAPACITY</th>\n",
       "      <th>SEATS_SOLD</th>\n",
       "      <th>LOAD_FACTOR</th>\n",
       "      <th>TICKET_PRICE</th>\n",
       "      <th>FLIGHT_REVENUE</th>\n",
       "      <th>DELAY_CATEGORY</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2023-10-29</td>\n",
       "      <td>10</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>EY</td>\n",
       "      <td>MCT</td>\n",
       "      <td>JFK</td>\n",
       "      <td>MCT-JFK</td>\n",
       "      <td>19</td>\n",
       "      <td>1</td>\n",
       "      <td>7804</td>\n",
       "      <td>135.0</td>\n",
       "      <td>180</td>\n",
       "      <td>105</td>\n",
       "      <td>0.5839</td>\n",
       "      <td>1080.36</td>\n",
       "      <td>113437.80</td>\n",
       "      <td>MAJOR_DELAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2023-10-04</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>EY</td>\n",
       "      <td>SHJ</td>\n",
       "      <td>JFK</td>\n",
       "      <td>SHJ-JFK</td>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>1051</td>\n",
       "      <td>175.0</td>\n",
       "      <td>120</td>\n",
       "      <td>103</td>\n",
       "      <td>0.8612</td>\n",
       "      <td>279.92</td>\n",
       "      <td>28831.76</td>\n",
       "      <td>MAJOR_DELAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2023-05-06</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>G9</td>\n",
       "      <td>JFK</td>\n",
       "      <td>CDG</td>\n",
       "      <td>JFK-CDG</td>\n",
       "      <td>19</td>\n",
       "      <td>1</td>\n",
       "      <td>6013</td>\n",
       "      <td>94.0</td>\n",
       "      <td>220</td>\n",
       "      <td>193</td>\n",
       "      <td>0.8800</td>\n",
       "      <td>943.98</td>\n",
       "      <td>182188.14</td>\n",
       "      <td>MAJOR_DELAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2023-10-05</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>FZ</td>\n",
       "      <td>SHJ</td>\n",
       "      <td>MCT</td>\n",
       "      <td>SHJ-MCT</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>734</td>\n",
       "      <td>3.0</td>\n",
       "      <td>180</td>\n",
       "      <td>128</td>\n",
       "      <td>0.7163</td>\n",
       "      <td>173.25</td>\n",
       "      <td>22176.00</td>\n",
       "      <td>MINOR_DELAY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2023-07-14</td>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>EY</td>\n",
       "      <td>BAH</td>\n",
       "      <td>DOH</td>\n",
       "      <td>BAH-DOH</td>\n",
       "      <td>12</td>\n",
       "      <td>0</td>\n",
       "      <td>1150</td>\n",
       "      <td>7.0</td>\n",
       "      <td>120</td>\n",
       "      <td>93</td>\n",
       "      <td>0.7755</td>\n",
       "      <td>264.19</td>\n",
       "      <td>24569.67</td>\n",
       "      <td>MINOR_DELAY</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      FL_DATE  MONTH  DAY_OF_WEEK  ...  TICKET_PRICE FLIGHT_REVENUE DELAY_CATEGORY\n",
       "0  2023-10-29     10            6  ...       1080.36      113437.80    MAJOR_DELAY\n",
       "1  2023-10-04     10            2  ...        279.92       28831.76    MAJOR_DELAY\n",
       "2  2023-05-06      5            5  ...        943.98      182188.14    MAJOR_DELAY\n",
       "3  2023-10-05     10            3  ...        173.25       22176.00    MINOR_DELAY\n",
       "4  2023-07-14      7            4  ...        264.19       24569.67    MINOR_DELAY\n",
       "\n",
       "[5 rows x 18 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# ============================================================\n",
    "# ARIA - 02_ML_Models\n",
    "# Cell 1: Load processed data from Delta Lake\n",
    "# ============================================================\n",
    "\n",
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
    "from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor\n",
    "from xgboost import XGBRegressor\n",
    "\n",
    "print(\"Loading data from Delta Lake table...\")\n",
    "\n",
    "# Load from Delta table we saved in previous notebook\n",
    "df = spark.sql(\"SELECT * FROM aria_flights\").toPandas()\n",
    "\n",
    "print(f\"Loaded {len(df):,} records\")\n",
    "print(f\"Columns: {list(df.columns)}\")\n",
    "df.head()"
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
     "finishTime": 1782501919853,
     "inputWidgets": {},
     "nuid": "f390cf3a-548d-4b9a-b62f-da16bcecfce2",
     "showTitle": true,
     "startTime": 1782501919398,
     "submitTime": 1782501919309,
     "tableResultSettingsMap": {},
     "title": "Exploratory Data Analysis (EDA):"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==================================================\nARIA - Exploratory Data Analysis\n==================================================\n\n\uD83D\uDCCA Dataset Shape: (500000, 18)\n\n\uD83D\uDCCA Missing Values:\nFL_DATE           0\nMONTH             0\nDAY_OF_WEEK       0\nIS_WEEKEND        0\nAIRLINE           0\nORIGIN            0\nDEST              0\nROUTE             0\nDEP_HOUR          0\nIS_PEAK_HOUR      0\nDISTANCE          0\nDEP_DELAY         0\nSEATS_CAPACITY    0\nSEATS_SOLD        0\nLOAD_FACTOR       0\nTICKET_PRICE      0\nFLIGHT_REVENUE    0\nDELAY_CATEGORY    0\ndtype: int64\n\n\uD83D\uDCCA Revenue Statistics:\n  Average Ticket Price:   $634.05\n  Max Ticket Price:       $1253.93\n  Min Ticket Price:       $57.42\n  Average Load Factor:    76.5%\n  Average Flight Revenue: $99,146.10\n  Total Revenue (all flights): $49,573,048,098\n\n\uD83D\uDCCA Top 10 Busiest Routes:\nROUTE\nCDG-LHR    889175\nLHR-CDG    889169\nDXB-AUH    887604\nMCT-DXB    885999\nJFK-BAH    885309\nDOH-JFK    882641\nJFK-MCT    881650\nBAH-AUH    880136\nKWI-AUH    878801\nAUH-MCT    876711\nName: SEATS_SOLD, dtype: int64\n\n\uD83D\uDCCA Revenue by Airline:\nAIRLINE\nEK    99436.821781\nG9    99275.687977\nEY    99161.024213\nWY    98986.487746\nFZ    98873.417925\nName: FLIGHT_REVENUE, dtype: float64\n\n\uD83D\uDCCA Peak vs Off-Peak Revenue:\nIS_PEAK_HOUR\n0    616.309783\n1    660.176279\nName: TICKET_PRICE, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 2: EDA - Understanding the data before modeling\n",
    "# This is critical - always explore before building models\n",
    "# ============================================================\n",
    "\n",
    "print(\"=\" * 50)\n",
    "print(\"ARIA - Exploratory Data Analysis\")\n",
    "print(\"=\" * 50)\n",
    "\n",
    "# Basic statistics\n",
    "print(\"\\n\uD83D\uDCCA Dataset Shape:\", df.shape)\n",
    "print(\"\\n\uD83D\uDCCA Missing Values:\")\n",
    "print(df.isnull().sum())\n",
    "\n",
    "print(\"\\n\uD83D\uDCCA Revenue Statistics:\")\n",
    "print(f\"  Average Ticket Price:   ${df['TICKET_PRICE'].mean():.2f}\")\n",
    "print(f\"  Max Ticket Price:       ${df['TICKET_PRICE'].max():.2f}\")\n",
    "print(f\"  Min Ticket Price:       ${df['TICKET_PRICE'].min():.2f}\")\n",
    "print(f\"  Average Load Factor:    {df['LOAD_FACTOR'].mean():.1%}\")\n",
    "print(f\"  Average Flight Revenue: ${df['FLIGHT_REVENUE'].mean():,.2f}\")\n",
    "print(f\"  Total Revenue (all flights): ${df['FLIGHT_REVENUE'].sum():,.0f}\")\n",
    "\n",
    "print(\"\\n\uD83D\uDCCA Top 10 Busiest Routes:\")\n",
    "print(df.groupby('ROUTE')['SEATS_SOLD'].sum().sort_values(ascending=False).head(10))\n",
    "\n",
    "print(\"\\n\uD83D\uDCCA Revenue by Airline:\")\n",
    "print(df.groupby('AIRLINE')['FLIGHT_REVENUE'].mean().sort_values(ascending=False))\n",
    "\n",
    "print(\"\\n\uD83D\uDCCA Peak vs Off-Peak Revenue:\")\n",
    "print(df.groupby('IS_PEAK_HOUR')['TICKET_PRICE'].mean())"
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
     "finishTime": 1782501999465,
     "inputWidgets": {},
     "nuid": "981d69a2-c502-495e-852e-8a0388c5f781",
     "showTitle": true,
     "startTime": 1782501985105,
     "submitTime": 1782501984960,
     "tableResultSettingsMap": {},
     "title": "Model 1: Demand Forecasting:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Building Demand Forecasting Model...\nThis predicts SEATS_SOLD based on route, time, price features\nTraining samples: 400,000\nTesting samples:  100,000\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/06/26 19:26:34 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:\n - mlflow (current: 3.14.0, required: mlflow==2.13.1)\nTo fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.\n2026/06/26 19:26:34 WARNING mlflow.models.model: Model logged without a signature. Signatures will be required for upcoming model registry features as they validate model inputs and denote the expected schema of model outputs. Please visit https://www.mlflow.org/docs/2.13.1/models.html#set-signature-on-logged-model for instructions on setting a model signature on your logged model.\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5034a19a07e14d39956f9a6455968a8a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Uploading artifacts:   0%|          | 0/9 [00:00<?, ?it/s]"
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
      "\n==================================================\nDEMAND FORECASTING MODEL RESULTS\n==================================================\nMAE  (Mean Abs Error):     18.04 seats\nRMSE (Root Mean Sq Error): 22.70 seats\nR2   (Accuracy Score):     0.8852\nMAPE (% Error):            12.19%\nForecast Accuracy:         87.8%\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 3: MODEL 1 - Demand Forecasting\n",
    "# Goal: Predict how many seats will be sold on a flight\n",
    "# This helps airlines decide how many seats to release\n",
    "# ============================================================\n",
    "\n",
    "print(\"Building Demand Forecasting Model...\")\n",
    "print(\"This predicts SEATS_SOLD based on route, time, price features\")\n",
    "\n",
    "# --- Feature Selection ---\n",
    "# These are the features that influence demand\n",
    "DEMAND_FEATURES = [\n",
    "    'MONTH',         # Seasonal demand patterns\n",
    "    'DAY_OF_WEEK',   # Weekly patterns\n",
    "    'IS_WEEKEND',    # Weekend vs weekday\n",
    "    'DEP_HOUR',      # Time of day\n",
    "    'IS_PEAK_HOUR',  # Peak travel hours\n",
    "    'DISTANCE',      # Longer routes = different demand\n",
    "    'TICKET_PRICE',  # Price affects demand (elasticity)\n",
    "    'SEATS_CAPACITY' # Total seats available\n",
    "]\n",
    "\n",
    "TARGET_DEMAND = 'SEATS_SOLD'\n",
    "\n",
    "# --- Encode Airline (text → number for ML) ---\n",
    "le = LabelEncoder()\n",
    "df['AIRLINE_ENC'] = le.fit_transform(df['AIRLINE'])\n",
    "DEMAND_FEATURES.append('AIRLINE_ENC')\n",
    "\n",
    "# --- Split Data ---\n",
    "X_demand = df[DEMAND_FEATURES]\n",
    "y_demand = df[TARGET_DEMAND]\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X_demand, y_demand,\n",
    "    test_size=0.2,      # 80% train, 20% test\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "print(f\"Training samples: {len(X_train):,}\")\n",
    "print(f\"Testing samples:  {len(X_test):,}\")\n",
    "\n",
    "# --- Train XGBoost Model ---\n",
    "# XGBoost is industry standard for tabular data\n",
    "# Used by winning teams in most Kaggle competitions\n",
    "\n",
    "with mlflow.start_run(run_name=\"demand_forecasting_xgb\"):\n",
    "\n",
    "    model_demand = XGBRegressor(\n",
    "        n_estimators=100,      # 100 decision trees\n",
    "        max_depth=6,           # Tree depth\n",
    "        learning_rate=0.1,     # Step size\n",
    "        random_state=42,\n",
    "        verbosity=0\n",
    "    )\n",
    "\n",
    "    model_demand.fit(X_train, y_train)\n",
    "\n",
    "    # Predictions\n",
    "    y_pred_demand = model_demand.predict(X_test)\n",
    "\n",
    "    # Metrics\n",
    "    mae  = mean_absolute_error(y_test, y_pred_demand)\n",
    "    rmse = np.sqrt(mean_squared_error(y_test, y_pred_demand))\n",
    "    r2   = r2_score(y_test, y_pred_demand)\n",
    "    mape = np.mean(np.abs((y_test - y_pred_demand) / y_test)) * 100\n",
    "\n",
    "    # Log to MLflow\n",
    "    mlflow.log_metric(\"MAE\",  mae)\n",
    "    mlflow.log_metric(\"RMSE\", rmse)\n",
    "    mlflow.log_metric(\"R2\",   r2)\n",
    "    mlflow.log_metric(\"MAPE\", mape)\n",
    "    mlflow.sklearn.log_model(model_demand, \"demand_model\")\n",
    "\n",
    "    print(\"\\n\" + \"=\" * 50)\n",
    "    print(\"DEMAND FORECASTING MODEL RESULTS\")\n",
    "    print(\"=\" * 50)\n",
    "    print(f\"MAE  (Mean Abs Error):     {mae:.2f} seats\")\n",
    "    print(f\"RMSE (Root Mean Sq Error): {rmse:.2f} seats\")\n",
    "    print(f\"R2   (Accuracy Score):     {r2:.4f}\")\n",
    "    print(f\"MAPE (% Error):            {mape:.2f}%\")\n",
    "    print(f\"Forecast Accuracy:         {100-mape:.1f}%\")"
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
     "finishTime": 1782502102788,
     "inputWidgets": {},
     "nuid": "f7f17e76-5eab-4ca4-8592-4280681616ab",
     "showTitle": true,
     "startTime": 1782502094607,
     "submitTime": 1782502094440,
     "tableResultSettingsMap": {},
     "title": "Model 2: Dynamic Pricing:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Building Dynamic Pricing Model...\nThis predicts TICKET_PRICE based on demand signals\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/06/26 19:28:21 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:\n - mlflow (current: 3.14.0, required: mlflow==2.13.1)\nTo fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.\n2026/06/26 19:28:21 WARNING mlflow.models.model: Model logged without a signature. Signatures will be required for upcoming model registry features as they validate model inputs and denote the expected schema of model outputs. Please visit https://www.mlflow.org/docs/2.13.1/models.html#set-signature-on-logged-model for instructions on setting a model signature on your logged model.\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "46f32703cf424829aa89f4c2fbfada4e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Uploading artifacts:   0%|          | 0/9 [00:00<?, ?it/s]"
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
      "\n==================================================\nDYNAMIC PRICING MODEL RESULTS\n==================================================\nMAE  (Mean Abs Error):     $12.12\nRMSE (Root Mean Sq Error): $15.20\nR2   (Accuracy Score):     0.9969\nMAPE (% Error):            2.51%\nPricing Accuracy:          97.5%\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 4: MODEL 2 - Dynamic Pricing Model\n",
    "# Goal: Predict optimal ticket price for maximum revenue\n",
    "# This is the core of airline revenue management\n",
    "# ============================================================\n",
    "\n",
    "print(\"Building Dynamic Pricing Model...\")\n",
    "print(\"This predicts TICKET_PRICE based on demand signals\")\n",
    "\n",
    "PRICING_FEATURES = [\n",
    "    'MONTH',\n",
    "    'DAY_OF_WEEK',\n",
    "    'IS_WEEKEND',\n",
    "    'DEP_HOUR',\n",
    "    'IS_PEAK_HOUR',\n",
    "    'DISTANCE',\n",
    "    'LOAD_FACTOR',    # How full the flight is\n",
    "    'SEATS_CAPACITY',\n",
    "    'AIRLINE_ENC'\n",
    "]\n",
    "\n",
    "TARGET_PRICE = 'TICKET_PRICE'\n",
    "\n",
    "X_price = df[PRICING_FEATURES]\n",
    "y_price = df[TARGET_PRICE]\n",
    "\n",
    "X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(\n",
    "    X_price, y_price,\n",
    "    test_size=0.2,\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "with mlflow.start_run(run_name=\"dynamic_pricing_xgb\"):\n",
    "\n",
    "    model_pricing = XGBRegressor(\n",
    "        n_estimators=100,\n",
    "        max_depth=6,\n",
    "        learning_rate=0.1,\n",
    "        random_state=42,\n",
    "        verbosity=0\n",
    "    )\n",
    "\n",
    "    model_pricing.fit(X_train_p, y_train_p)\n",
    "\n",
    "    y_pred_price = model_pricing.predict(X_test_p)\n",
    "\n",
    "    mae_p  = mean_absolute_error(y_test_p, y_pred_price)\n",
    "    rmse_p = np.sqrt(mean_squared_error(y_test_p, y_pred_price))\n",
    "    r2_p   = r2_score(y_test_p, y_pred_price)\n",
    "    mape_p = np.mean(np.abs((y_test_p - y_pred_price) / y_test_p)) * 100\n",
    "\n",
    "    mlflow.log_metric(\"MAE\",  mae_p)\n",
    "    mlflow.log_metric(\"RMSE\", rmse_p)\n",
    "    mlflow.log_metric(\"R2\",   r2_p)\n",
    "    mlflow.log_metric(\"MAPE\", mape_p)\n",
    "    mlflow.sklearn.log_model(model_pricing, \"pricing_model\")\n",
    "\n",
    "    print(\"\\n\" + \"=\" * 50)\n",
    "    print(\"DYNAMIC PRICING MODEL RESULTS\")\n",
    "    print(\"=\" * 50)\n",
    "    print(f\"MAE  (Mean Abs Error):     ${mae_p:.2f}\")\n",
    "    print(f\"RMSE (Root Mean Sq Error): ${rmse_p:.2f}\")\n",
    "    print(f\"R2   (Accuracy Score):     {r2_p:.4f}\")\n",
    "    print(f\"MAPE (% Error):            {mape_p:.2f}%\")\n",
    "    print(f\"Pricing Accuracy:          {100-mape_p:.1f}%\")"
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
     "finishTime": 1782502169870,
     "inputWidgets": {},
     "nuid": "3f6e62d8-6336-46b2-82b1-3ec7093d0d23",
     "showTitle": true,
     "startTime": 1782502160417,
     "submitTime": 1782502160316,
     "tableResultSettingsMap": {},
     "title": "Model 3: Revenue Optimizer:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Building Revenue Optimization Model...\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/06/26 19:29:28 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:\n - mlflow (current: 3.14.0, required: mlflow==2.13.1)\nTo fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.\n2026/06/26 19:29:28 WARNING mlflow.models.model: Model logged without a signature. Signatures will be required for upcoming model registry features as they validate model inputs and denote the expected schema of model outputs. Please visit https://www.mlflow.org/docs/2.13.1/models.html#set-signature-on-logged-model for instructions on setting a model signature on your logged model.\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9b201f1222c54200982ca1ca29154040",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Uploading artifacts:   0%|          | 0/9 [00:00<?, ?it/s]"
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
      "\n==================================================\nREVENUE OPTIMIZATION MODEL RESULTS\n==================================================\nMAE  (Mean Abs Error):     $348.28\nRMSE (Root Mean Sq Error): $515.16\nR2   (Accuracy Score):     0.9999\nMAPE (% Error):            0.46%\nRevenue Prediction Accuracy: 99.5%\n\n==================================================\nALL 3 MODELS TRAINED & LOGGED TO MLFLOW!\n==================================================\nModel 1: Demand Forecasting  → predicts seats sold\nModel 2: Dynamic Pricing     → predicts optimal price\nModel 3: Revenue Optimizer   → predicts total revenue\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 5: MODEL 3 - Revenue Optimization\n",
    "# Goal: Predict total flight revenue\n",
    "# Combines demand + pricing signals to maximize revenue\n",
    "# ============================================================\n",
    "\n",
    "print(\"Building Revenue Optimization Model...\")\n",
    "\n",
    "REVENUE_FEATURES = [\n",
    "    'MONTH',\n",
    "    'DAY_OF_WEEK',\n",
    "    'IS_WEEKEND',\n",
    "    'DEP_HOUR',\n",
    "    'IS_PEAK_HOUR',\n",
    "    'DISTANCE',\n",
    "    'LOAD_FACTOR',\n",
    "    'SEATS_CAPACITY',\n",
    "    'SEATS_SOLD',\n",
    "    'TICKET_PRICE',\n",
    "    'AIRLINE_ENC'\n",
    "]\n",
    "\n",
    "TARGET_REVENUE = 'FLIGHT_REVENUE'\n",
    "\n",
    "X_rev = df[REVENUE_FEATURES]\n",
    "y_rev = df[TARGET_REVENUE]\n",
    "\n",
    "X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(\n",
    "    X_rev, y_rev,\n",
    "    test_size=0.2,\n",
    "    random_state=42\n",
    ")\n",
    "\n",
    "with mlflow.start_run(run_name=\"revenue_optimization_xgb\"):\n",
    "\n",
    "    model_revenue = XGBRegressor(\n",
    "        n_estimators=150,\n",
    "        max_depth=7,\n",
    "        learning_rate=0.08,\n",
    "        random_state=42,\n",
    "        verbosity=0\n",
    "    )\n",
    "\n",
    "    model_revenue.fit(X_train_r, y_train_r)\n",
    "\n",
    "    y_pred_rev = model_revenue.predict(X_test_r)\n",
    "\n",
    "    mae_r  = mean_absolute_error(y_test_r, y_pred_rev)\n",
    "    rmse_r = np.sqrt(mean_squared_error(y_test_r, y_pred_rev))\n",
    "    r2_r   = r2_score(y_test_r, y_pred_rev)\n",
    "    mape_r = np.mean(np.abs((y_test_r - y_pred_rev) / y_test_r)) * 100\n",
    "\n",
    "    mlflow.log_metric(\"MAE\",  mae_r)\n",
    "    mlflow.log_metric(\"RMSE\", rmse_r)\n",
    "    mlflow.log_metric(\"R2\",   r2_r)\n",
    "    mlflow.log_metric(\"MAPE\", mape_r)\n",
    "    mlflow.sklearn.log_model(model_revenue, \"revenue_model\")\n",
    "\n",
    "    print(\"\\n\" + \"=\" * 50)\n",
    "    print(\"REVENUE OPTIMIZATION MODEL RESULTS\")\n",
    "    print(\"=\" * 50)\n",
    "    print(f\"MAE  (Mean Abs Error):     ${mae_r:,.2f}\")\n",
    "    print(f\"RMSE (Root Mean Sq Error): ${rmse_r:,.2f}\")\n",
    "    print(f\"R2   (Accuracy Score):     {r2_r:.4f}\")\n",
    "    print(f\"MAPE (% Error):            {mape_r:.2f}%\")\n",
    "    print(f\"Revenue Prediction Accuracy: {100-mape_r:.1f}%\")\n",
    "\n",
    "    print(\"\\n\" + \"=\" * 50)\n",
    "    print(\"ALL 3 MODELS TRAINED & LOGGED TO MLFLOW!\")\n",
    "    print(\"=\" * 50)\n",
    "    print(\"Model 1: Demand Forecasting  → predicts seats sold\")\n",
    "    print(\"Model 2: Dynamic Pricing     → predicts optimal price\")\n",
    "    print(\"Model 3: Revenue Optimizer   → predicts total revenue\")"
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
    "experimentId": "2784440046001158",
    "pythonIndentUnit": 4
   },
   "notebookName": "02_ML_Models",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}