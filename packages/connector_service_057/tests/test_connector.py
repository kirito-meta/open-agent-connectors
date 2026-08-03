"""
Unit tests for Service057 Connector.
"""

import pytest
from service_057.connector import Service057Connector

def test_connection_success():
    connector = Service057Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service057Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
