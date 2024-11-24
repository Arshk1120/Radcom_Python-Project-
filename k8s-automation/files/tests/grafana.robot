*** Settings ***
Library    utils/grafana_api.py

*** Test Cases ***
Configure Grafana
    Login To Grafana
    Configure Datasource
    Create Dashboard

