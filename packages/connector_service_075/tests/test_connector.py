"""
Unit tests for Service075 Connector.
"""

import pytest
from service_075.connector import Service075Connector

def test_connection_success():
    connector = Service075Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service075Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
