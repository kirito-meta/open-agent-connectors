"""
Unit tests for Service001 Connector.
"""

import pytest
from service_001.connector import Service001Connector

def test_connection_success():
    connector = Service001Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service001Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
