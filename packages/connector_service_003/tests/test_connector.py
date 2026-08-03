"""
Unit tests for Service003 Connector.
"""

import pytest
from service_003.connector import Service003Connector

def test_connection_success():
    connector = Service003Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service003Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
