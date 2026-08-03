"""
Unit tests for Service053 Connector.
"""

import pytest
from service_053.connector import Service053Connector

def test_connection_success():
    connector = Service053Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service053Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
