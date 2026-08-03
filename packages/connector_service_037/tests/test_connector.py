"""
Unit tests for Service037 Connector.
"""

import pytest
from service_037.connector import Service037Connector

def test_connection_success():
    connector = Service037Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service037Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
