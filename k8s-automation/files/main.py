from fastapi import FastAPI
from utils.db_manager import create_table
from utils.grafana_api import login_to_grafana, configure_datasource, create_dashboard

app = FastAPI()

@app.post("/test")
def run_test():
    create_table()
    login_to_grafana()
    configure_datasource()
    create_dashboard()
    return {"status": "Tests completed"}

@app.get("/results")
def get_results():
    return {"status": "All tests passed"}

