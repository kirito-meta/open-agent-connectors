"""
Unit tests for Service054 Connector.
"""

import pytest
from service_054.connector import Service054Connector

def test_connection_success():
    connector = Service054Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service054Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
