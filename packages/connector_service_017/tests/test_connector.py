"""
Unit tests for Service017 Connector.
"""

import pytest
from service_017.connector import Service017Connector

def test_connection_success():
    connector = Service017Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service017Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
