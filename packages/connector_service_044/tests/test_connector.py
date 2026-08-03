"""
Unit tests for Service044 Connector.
"""

import pytest
from service_044.connector import Service044Connector

def test_connection_success():
    connector = Service044Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service044Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
