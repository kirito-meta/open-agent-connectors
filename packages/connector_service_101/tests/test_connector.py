"""
Unit tests for Service101 Connector.
"""

import pytest
from service_101.connector import Service101Connector

def test_connection_success():
    connector = Service101Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service101Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
