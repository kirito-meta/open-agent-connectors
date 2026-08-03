"""
Unit tests for Service038 Connector.
"""

import pytest
from service_038.connector import Service038Connector

def test_connection_success():
    connector = Service038Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service038Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
