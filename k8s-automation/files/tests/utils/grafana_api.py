import requests
def login_to_grafana():
    url = "http://localhost:3000/api/login"
    data = {"user": "admin", "password": "arshdeep"}
    response = requests.post(url, json=data)
    return response.status_code == 200
def configure_datasource():
    url = "http://localhost:3000/api/datasources"
    headers = {"Authorization": "Bearer adminpassword", "Content-Type": "application/json"}
    data = {
        "name": "MariaDB",
        "type": "mysql",
        "url": "my-mariadb:3306",
        "access": "proxy",
        "database": "testdb",
        "user": "root",
        "password": "arshdeep"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code == 200
def create_dashboard():
    url = "http://localhost:3000/api/dashboards/db"
    headers = {"Authorization": "Bearer adminpassword", "Content-Type": "application/json"}
    data = {
        "dashboard": {
            "id": None,
            "title": "Metrics Dashboard",
            "panels": [
                {
                    "type": "timeseries",
                    "title": "Metric Values",
                    "datasource": "MariaDB",
                    "targets": [{"rawSql": "SELECT UNIX_TIMESTAMP(timestamp) as time, value FROM metrics"}]
                }
            ]
        },
        "folderId": 0,
        "overwrite": True
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code == 200

