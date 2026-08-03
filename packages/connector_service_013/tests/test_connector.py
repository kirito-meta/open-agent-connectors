"""
Unit tests for Service013 Connector.
"""

import pytest
from service_013.connector import Service013Connector

def test_connection_success():
    connector = Service013Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service013Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
