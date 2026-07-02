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
     "finishTime": 1782933823404,
     "inputWidgets": {},
     "nuid": "885c5b25-0f72-41d2-bef0-90bb66d327e5",
     "showTitle": false,
     "startTime": 1782933769664,
     "submitTime": 1782933740256,
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
      "\u001B[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\nlangchain-community 0.0.38 requires langchain-core<0.2.0,>=0.1.52, but you have langchain-core 1.4.8 which is incompatible.\nlangchain-community 0.0.38 requires langsmith<0.2.0,>=0.1.0, but you have langsmith 0.9.5 which is incompatible.\nlangchain-text-splitters 0.0.2 requires langchain-core<0.3,>=0.1.28, but you have langchain-core 1.4.8 which is incompatible.\nydata-profiling 4.5.1 requires pydantic<2,>=1.8.1, but you have pydantic 2.13.4 which is incompatible.\u001B[0m\u001B[31m\n\u001B[0m\u001B[43mNote: you may need to restart the kernel using %restart_python or dbutils.library.restartPython() to use updated packages.\u001B[0m\n"
     ]
    }
   ],
   "source": [
    "%pip install langgraph langchain langchain-openai --quiet\n",
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
     "finishTime": 1782934020281,
     "inputWidgets": {},
     "nuid": "a0c3f2ec-2cac-4ab6-adae-e50790d3d11b",
     "showTitle": true,
     "startTime": 1782933823477,
     "submitTime": 1782933740342,
     "tableResultSettingsMap": {},
     "title": "Setup + Retrain Models:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading data and training models...\n"
     ]
    },
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/07/01 19:25:23 WARNING mlflow.models.model: Model logged without a signature. Signatures will be required for upcoming model registry features as they validate model inputs and denote the expected schema of model outputs. Please visit https://www.mlflow.org/docs/2.13.1/models.html#set-signature-on-logged-model for instructions on setting a model signature on your logged model.\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e34e557a037742fcbf1395d7887a5e6c",
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
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/07/01 19:26:00 WARNING mlflow.models.model: Model logged without a signature. Signatures will be required for upcoming model registry features as they validate model inputs and denote the expected schema of model outputs. Please visit https://www.mlflow.org/docs/2.13.1/models.html#set-signature-on-logged-model for instructions on setting a model signature on your logged model.\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f32aa4b033fe4ce5b9d8795572da2356",
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
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026/07/01 19:26:59 WARNING mlflow.models.model: Model logged without a signature. Signatures will be required for upcoming model registry features as they validate model inputs and denote the expected schema of model outputs. Please visit https://www.mlflow.org/docs/2.13.1/models.html#set-signature-on-logged-model for instructions on setting a model signature on your logged model.\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a5019dbaf7d34163a5ea72de8526c404",
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
      "✅ All models trained!\n✅ All functions ready!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import mlflow\n",
    "import mlflow.xgboost\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import r2_score\n",
    "from xgboost import XGBRegressor\n",
    "from typing import TypedDict, Annotated\n",
    "import operator\n",
    "\n",
    "print(\"Loading data and training models...\")\n",
    "df = spark.sql(\"SELECT * FROM aria_flights\").toPandas()\n",
    "\n",
    "le = LabelEncoder()\n",
    "df['AIRLINE_ENC'] = le.fit_transform(df['AIRLINE'])\n",
    "\n",
    "mlflow.set_experiment(\"/ARIA-Experiment\")\n",
    "TRUSTED_TYPES = [\"xgboost.core.Booster\", \"xgboost.sklearn.XGBRegressor\"]\n",
    "\n",
    "# Train all 3 models\n",
    "def train_model(X, y, run_name, **kwargs):\n",
    "    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "    with mlflow.start_run(run_name=run_name) as r:\n",
    "        model = XGBRegressor(**kwargs, random_state=42, verbosity=0)\n",
    "        model.fit(X_tr, y_tr)\n",
    "        mlflow.log_metric(\"R2\", r2_score(y_te, model.predict(X_te)))\n",
    "        mlflow.xgboost.log_model(model, run_name)\n",
    "    return model\n",
    "\n",
    "model_demand = train_model(\n",
    "    df[['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR','IS_PEAK_HOUR',\n",
    "        'DISTANCE','TICKET_PRICE','SEATS_CAPACITY','AIRLINE_ENC']],\n",
    "    df['SEATS_SOLD'], \"demand_model\",\n",
    "    n_estimators=100, max_depth=6, learning_rate=0.1\n",
    ")\n",
    "\n",
    "model_pricing = train_model(\n",
    "    df[['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR','IS_PEAK_HOUR',\n",
    "        'DISTANCE','LOAD_FACTOR','SEATS_CAPACITY','AIRLINE_ENC']],\n",
    "    df['TICKET_PRICE'], \"pricing_model\",\n",
    "    n_estimators=100, max_depth=6, learning_rate=0.1\n",
    ")\n",
    "\n",
    "model_revenue = train_model(\n",
    "    df[['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR','IS_PEAK_HOUR',\n",
    "        'DISTANCE','LOAD_FACTOR','SEATS_CAPACITY','SEATS_SOLD','TICKET_PRICE','AIRLINE_ENC']],\n",
    "    df['FLIGHT_REVENUE'], \"revenue_model\",\n",
    "    n_estimators=150, max_depth=7, learning_rate=0.08\n",
    ")\n",
    "\n",
    "print(\"✅ All models trained!\")\n",
    "\n",
    "# Define tool functions\n",
    "def get_features(row, cols):\n",
    "    return pd.DataFrame([row], columns=cols)\n",
    "\n",
    "def forecast_demand(route, month, day_of_week, is_weekend,\n",
    "                    dep_hour, distance, ticket_price, seats_capacity, airline):\n",
    "    enc  = list(le.classes_).index(airline) if airline in le.classes_ else 0\n",
    "    peak = 1 if (7<=dep_hour<=9) or (17<=dep_hour<=19) else 0\n",
    "    f = get_features([month,day_of_week,is_weekend,dep_hour,peak,\n",
    "                      distance,ticket_price,seats_capacity,enc],\n",
    "                     ['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR','IS_PEAK_HOUR',\n",
    "                      'DISTANCE','TICKET_PRICE','SEATS_CAPACITY','AIRLINE_ENC'])\n",
    "    seats = int(model_demand.predict(f)[0])\n",
    "    lf    = round(seats/seats_capacity, 3)\n",
    "    return {\"predicted_seats_sold\": seats, \"load_factor\": lf,\n",
    "            \"demand_level\": \"HIGH\" if lf>0.85 else \"MEDIUM\" if lf>0.65 else \"LOW\"}\n",
    "\n",
    "def recommend_price(month, day_of_week, is_weekend, dep_hour,\n",
    "                    distance, load_factor, seats_capacity, airline):\n",
    "    enc  = list(le.classes_).index(airline) if airline in le.classes_ else 0\n",
    "    peak = 1 if (7<=dep_hour<=9) or (17<=dep_hour<=19) else 0\n",
    "    f = get_features([month,day_of_week,is_weekend,dep_hour,peak,\n",
    "                      distance,load_factor,seats_capacity,enc],\n",
    "                     ['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR','IS_PEAK_HOUR',\n",
    "                      'DISTANCE','LOAD_FACTOR','SEATS_CAPACITY','AIRLINE_ENC'])\n",
    "    price = round(float(model_pricing.predict(f)[0]), 2)\n",
    "    return {\"recommended_price\": price,\n",
    "            \"pricing_strategy\": \"PREMIUM\" if price>500 else \"STANDARD\" if price>250 else \"BUDGET\"}\n",
    "\n",
    "def optimize_revenue(month, day_of_week, is_weekend, dep_hour, distance,\n",
    "                     load_factor, seats_capacity, seats_sold, ticket_price, airline):\n",
    "    enc  = list(le.classes_).index(airline) if airline in le.classes_ else 0\n",
    "    peak = 1 if (7<=dep_hour<=9) or (17<=dep_hour<=19) else 0\n",
    "    f = get_features([month,day_of_week,is_weekend,dep_hour,peak,distance,\n",
    "                      load_factor,seats_capacity,seats_sold,ticket_price,enc],\n",
    "                     ['MONTH','DAY_OF_WEEK','IS_WEEKEND','DEP_HOUR','IS_PEAK_HOUR',\n",
    "                      'DISTANCE','LOAD_FACTOR','SEATS_CAPACITY','SEATS_SOLD','TICKET_PRICE','AIRLINE_ENC'])\n",
    "    rev  = round(float(model_revenue.predict(f)[0]), 2)\n",
    "    maxr = seats_capacity * ticket_price\n",
    "    eff  = round(rev/maxr*100, 1)\n",
    "    return {\"predicted_revenue\": rev, \"max_possible_revenue\": round(maxr,2),\n",
    "            \"revenue_efficiency\": f\"{eff}%\",\n",
    "            \"recommendation\": \"INCREASE PRICE\" if eff<70 else \"MAINTAIN\" if eff<90 else \"OPTIMAL\"}\n",
    "\n",
    "print(\"✅ All functions ready!\")"
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
     "finishTime": 1782934022376,
     "inputWidgets": {},
     "nuid": "e68b2f2d-d0c3-4f42-90fd-536a002753ce",
     "showTitle": true,
     "startTime": 1782934020336,
     "submitTime": 1782933740346,
     "tableResultSettingsMap": {},
     "title": "Define LangGraph State + Nodes:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ All 4 LangGraph nodes defined!\n   Node 1: demand_agent_node\n   Node 2: pricing_agent_node\n   Node 3: revenue_agent_node\n   Node 4: report_agent_node\n"
     ]
    }
   ],
   "source": [
    "from langgraph.graph import StateGraph, END\n",
    "from typing import TypedDict, Optional\n",
    "\n",
    "# ============================================================\n",
    "# LangGraph State\n",
    "# This is the \"memory\" shared across all agent nodes\n",
    "# Every node reads from and writes to this state\n",
    "# ============================================================\n",
    "\n",
    "class ARIAState(TypedDict):\n",
    "    # Input flight information\n",
    "    route:          str\n",
    "    month:          int\n",
    "    day_of_week:    int\n",
    "    is_weekend:     int\n",
    "    dep_hour:       int\n",
    "    distance:       int\n",
    "    ticket_price:   float\n",
    "    seats_capacity: int\n",
    "    airline:        str\n",
    "\n",
    "    # Outputs filled by each agent node\n",
    "    demand_result:  Optional[dict]\n",
    "    pricing_result: Optional[dict]\n",
    "    revenue_result: Optional[dict]\n",
    "    final_report:   Optional[str]\n",
    "\n",
    "\n",
    "# ============================================================\n",
    "# Node 1: Demand Forecasting Agent\n",
    "# In LangGraph, each \"node\" = one specialized agent\n",
    "# ============================================================\n",
    "def demand_agent_node(state: ARIAState) -> ARIAState:\n",
    "    print(\"\\n  \uD83D\uDD35 Node 1: Demand Forecasting Agent running...\")\n",
    "\n",
    "    result = forecast_demand(\n",
    "        route          = state[\"route\"],\n",
    "        month          = state[\"month\"],\n",
    "        day_of_week    = state[\"day_of_week\"],\n",
    "        is_weekend     = state[\"is_weekend\"],\n",
    "        dep_hour       = state[\"dep_hour\"],\n",
    "        distance       = state[\"distance\"],\n",
    "        ticket_price   = state[\"ticket_price\"],\n",
    "        seats_capacity = state[\"seats_capacity\"],\n",
    "        airline        = state[\"airline\"]\n",
    "    )\n",
    "\n",
    "    print(f\"     Result: {result}\")\n",
    "    return {**state, \"demand_result\": result}\n",
    "\n",
    "\n",
    "# ============================================================\n",
    "# Node 2: Dynamic Pricing Agent\n",
    "# Only runs AFTER demand agent completes\n",
    "# Uses load_factor from demand_result\n",
    "# ============================================================\n",
    "def pricing_agent_node(state: ARIAState) -> ARIAState:\n",
    "    print(\"\\n  \uD83D\uDFE1 Node 2: Dynamic Pricing Agent running...\")\n",
    "\n",
    "    result = recommend_price(\n",
    "        month          = state[\"month\"],\n",
    "        day_of_week    = state[\"day_of_week\"],\n",
    "        is_weekend     = state[\"is_weekend\"],\n",
    "        dep_hour       = state[\"dep_hour\"],\n",
    "        distance       = state[\"distance\"],\n",
    "        load_factor    = state[\"demand_result\"][\"load_factor\"],\n",
    "        seats_capacity = state[\"seats_capacity\"],\n",
    "        airline        = state[\"airline\"]\n",
    "    )\n",
    "\n",
    "    print(f\"     Result: {result}\")\n",
    "    return {**state, \"pricing_result\": result}\n",
    "\n",
    "\n",
    "# ============================================================\n",
    "# Node 3: Revenue Optimization Agent\n",
    "# Runs LAST — uses outputs from both previous agents\n",
    "# ============================================================\n",
    "def revenue_agent_node(state: ARIAState) -> ARIAState:\n",
    "    print(\"\\n  \uD83D\uDFE2 Node 3: Revenue Optimization Agent running...\")\n",
    "\n",
    "    result = optimize_revenue(\n",
    "        month          = state[\"month\"],\n",
    "        day_of_week    = state[\"day_of_week\"],\n",
    "        is_weekend     = state[\"is_weekend\"],\n",
    "        dep_hour       = state[\"dep_hour\"],\n",
    "        distance       = state[\"distance\"],\n",
    "        load_factor    = state[\"demand_result\"][\"load_factor\"],\n",
    "        seats_capacity = state[\"seats_capacity\"],\n",
    "        seats_sold     = state[\"demand_result\"][\"predicted_seats_sold\"],\n",
    "        ticket_price   = state[\"pricing_result\"][\"recommended_price\"],\n",
    "        airline        = state[\"airline\"]\n",
    "    )\n",
    "\n",
    "    print(f\"     Result: {result}\")\n",
    "    return {**state, \"revenue_result\": result}\n",
    "\n",
    "\n",
    "# ============================================================\n",
    "# Node 4: Report Generator\n",
    "# Final node — summarizes everything into business report\n",
    "# ============================================================\n",
    "def report_agent_node(state: ARIAState) -> ARIAState:\n",
    "    print(\"\\n  \uD83D\uDCCB Node 4: Report Generator running...\")\n",
    "\n",
    "    d = state[\"demand_result\"]\n",
    "    p = state[\"pricing_result\"]\n",
    "    r = state[\"revenue_result\"]\n",
    "    price_diff = p[\"recommended_price\"] - state[\"ticket_price\"]\n",
    "\n",
    "    report = f\"\"\"\n",
    "╔══════════════════════════════════════════════════╗\n",
    "║         ARIA LANGGRAPH FINAL REPORT              ║\n",
    "╠══════════════════════════════════════════════════╣\n",
    "║ Route:              {state['route']:<28} ║\n",
    "║ Airline:            {state['airline']:<28} ║\n",
    "╠══════════════════════════════════════════════════╣\n",
    "║ DEMAND ANALYSIS                                  ║\n",
    "║   Predicted Seats:  {str(d['predicted_seats_sold']):<28} ║\n",
    "║   Load Factor:      {str(round(d['load_factor']*100,1))+'%':<28} ║\n",
    "║   Demand Level:     {d['demand_level']:<28} ║\n",
    "╠══════════════════════════════════════════════════╣\n",
    "║ PRICING RECOMMENDATION                           ║\n",
    "║   Current Price:    ${str(state['ticket_price']):<27} ║\n",
    "║   Recommended:      ${str(p['recommended_price']):<27} ║\n",
    "║   Price Uplift:     +${str(round(price_diff,2)):<26} ║\n",
    "║   Strategy:         {p['pricing_strategy']:<28} ║\n",
    "╠══════════════════════════════════════════════════╣\n",
    "║ REVENUE OPTIMIZATION                             ║\n",
    "║   Predicted Rev:    ${str(round(r['predicted_revenue'],2)):<27} ║\n",
    "║   Max Possible:     ${str(r['max_possible_revenue']):<27} ║\n",
    "║   Efficiency:       {r['revenue_efficiency']:<28} ║\n",
    "║   Action:           {r['recommendation']:<28} ║\n",
    "╚══════════════════════════════════════════════════╝\"\"\"\n",
    "\n",
    "    print(report)\n",
    "    return {**state, \"final_report\": report}\n",
    "\n",
    "\n",
    "print(\"✅ All 4 LangGraph nodes defined!\")\n",
    "print(\"   Node 1: demand_agent_node\")\n",
    "print(\"   Node 2: pricing_agent_node\")\n",
    "print(\"   Node 3: revenue_agent_node\")\n",
    "print(\"   Node 4: report_agent_node\")"
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
     "finishTime": 1782934022674,
     "inputWidgets": {},
     "nuid": "3b64121c-d4f7-4fae-b9d0-4a7147240af2",
     "showTitle": true,
     "startTime": 1782934022391,
     "submitTime": 1782933740350,
     "tableResultSettingsMap": {},
     "title": "Build + Run the LangGraph:"
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ LangGraph compiled successfully!\n\n\uD83D\uDCCA Agent Flow:\n   demand_agent → pricing_agent → revenue_agent → report_agent → END\n\n=======================================================\n\uD83D\uDE80 RUNNING ARIA LANGGRAPH ORCHESTRATOR\n=======================================================\n\n  \uD83D\uDD35 Node 1: Demand Forecasting Agent running...\n     Result: {'predicted_seats_sold': 231, 'load_factor': 0.66, 'demand_level': 'MEDIUM'}\n\n  \uD83D\uDFE1 Node 2: Dynamic Pricing Agent running...\n     Result: {'recommended_price': 594.97, 'pricing_strategy': 'PREMIUM'}\n\n  \uD83D\uDFE2 Node 3: Revenue Optimization Agent running...\n     Result: {'predicted_revenue': 137100.69, 'max_possible_revenue': 208239.5, 'revenue_efficiency': '65.8%', 'recommendation': 'INCREASE PRICE'}\n\n  \uD83D\uDCCB Node 4: Report Generator running...\n\n╔══════════════════════════════════════════════════╗\n║         ARIA LANGGRAPH FINAL REPORT              ║\n╠══════════════════════════════════════════════════╣\n║ Route:              DXB-LHR                      ║\n║ Airline:            EK                           ║\n╠══════════════════════════════════════════════════╣\n║ DEMAND ANALYSIS                                  ║\n║   Predicted Seats:  231                          ║\n║   Load Factor:      66.0%                        ║\n║   Demand Level:     MEDIUM                       ║\n╠══════════════════════════════════════════════════╣\n║ PRICING RECOMMENDATION                           ║\n║   Current Price:    $450.0                       ║\n║   Recommended:      $594.97                      ║\n║   Price Uplift:     +$144.97                     ║\n║   Strategy:         PREMIUM                      ║\n╠══════════════════════════════════════════════════╣\n║ REVENUE OPTIMIZATION                             ║\n║   Predicted Rev:    $137100.69                   ║\n║   Max Possible:     $208239.5                    ║\n║   Efficiency:       65.8%                        ║\n║   Action:           INCREASE PRICE               ║\n╚══════════════════════════════════════════════════╝\n\n✅ LangGraph execution complete!\n   All 4 nodes executed in sequence\n   Final report generated: 1219 characters\n"
     ]
    }
   ],
   "source": [
    "# ============================================================\n",
    "# Cell 4: Build LangGraph — connect nodes into a graph\n",
    "# This defines the FLOW of how agents communicate\n",
    "# ============================================================\n",
    "\n",
    "# Create the graph\n",
    "workflow = StateGraph(ARIAState)\n",
    "\n",
    "# Add all agent nodes to the graph\n",
    "workflow.add_node(\"demand_agent\",  demand_agent_node)\n",
    "workflow.add_node(\"pricing_agent\", pricing_agent_node)\n",
    "workflow.add_node(\"revenue_agent\", revenue_agent_node)\n",
    "workflow.add_node(\"report_agent\",  report_agent_node)\n",
    "\n",
    "# Define edges — the ORDER agents run in\n",
    "# This is the \"orchestration\" part LangGraph manages\n",
    "workflow.set_entry_point(\"demand_agent\")           # Start here\n",
    "workflow.add_edge(\"demand_agent\",  \"pricing_agent\") # Then pricing\n",
    "workflow.add_edge(\"pricing_agent\", \"revenue_agent\") # Then revenue\n",
    "workflow.add_edge(\"revenue_agent\", \"report_agent\")  # Then report\n",
    "workflow.add_edge(\"report_agent\",  END)             # Then done\n",
    "\n",
    "# Compile the graph\n",
    "aria_graph = workflow.compile()\n",
    "\n",
    "print(\"✅ LangGraph compiled successfully!\")\n",
    "print(\"\\n\uD83D\uDCCA Agent Flow:\")\n",
    "print(\"   demand_agent → pricing_agent → revenue_agent → report_agent → END\")\n",
    "\n",
    "# ---- Run the graph ----\n",
    "print(\"\\n\" + \"=\"*55)\n",
    "print(\"\uD83D\uDE80 RUNNING ARIA LANGGRAPH ORCHESTRATOR\")\n",
    "print(\"=\"*55)\n",
    "\n",
    "initial_state = {\n",
    "    \"route\":          \"DXB-LHR\",\n",
    "    \"month\":          12,\n",
    "    \"day_of_week\":    4,\n",
    "    \"is_weekend\":     1,\n",
    "    \"dep_hour\":       8,\n",
    "    \"distance\":       3400,\n",
    "    \"ticket_price\":   450.0,\n",
    "    \"seats_capacity\": 350,\n",
    "    \"airline\":        \"EK\",\n",
    "    \"demand_result\":  None,\n",
    "    \"pricing_result\": None,\n",
    "    \"revenue_result\": None,\n",
    "    \"final_report\":   None\n",
    "}\n",
    "\n",
    "# Run the graph — LangGraph manages the entire flow\n",
    "final_state = aria_graph.invoke(initial_state)\n",
    "\n",
    "print(\"\\n✅ LangGraph execution complete!\")\n",
    "print(f\"   All 4 nodes executed in sequence\")\n",
    "print(f\"   Final report generated: {len(final_state['final_report'])} characters\")"
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
   "notebookName": "05_LangGraph_Orchestrator",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}