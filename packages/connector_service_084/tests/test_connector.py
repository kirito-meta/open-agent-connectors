"""
Unit tests for Service084 Connector.
"""

import pytest
from service_084.connector import Service084Connector

def test_connection_success():
    connector = Service084Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service084Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
