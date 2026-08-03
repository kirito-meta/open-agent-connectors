"""
Unit tests for Service059 Connector.
"""

import pytest
from service_059.connector import Service059Connector

def test_connection_success():
    connector = Service059Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service059Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
