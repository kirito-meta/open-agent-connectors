"""
Unit tests for Service050 Connector.
"""

import pytest
from service_050.connector import Service050Connector

def test_connection_success():
    connector = Service050Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service050Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
