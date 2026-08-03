"""
Unit tests for Service064 Connector.
"""

import pytest
from service_064.connector import Service064Connector

def test_connection_success():
    connector = Service064Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service064Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
