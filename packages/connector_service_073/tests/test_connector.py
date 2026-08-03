"""
Unit tests for Service073 Connector.
"""

import pytest
from service_073.connector import Service073Connector

def test_connection_success():
    connector = Service073Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service073Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
