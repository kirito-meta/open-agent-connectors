"""
Unit tests for Service063 Connector.
"""

import pytest
from service_063.connector import Service063Connector

def test_connection_success():
    connector = Service063Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service063Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
