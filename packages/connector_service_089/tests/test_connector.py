"""
Unit tests for Service089 Connector.
"""

import pytest
from service_089.connector import Service089Connector

def test_connection_success():
    connector = Service089Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service089Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
