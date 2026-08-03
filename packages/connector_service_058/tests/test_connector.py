"""
Unit tests for Service058 Connector.
"""

import pytest
from service_058.connector import Service058Connector

def test_connection_success():
    connector = Service058Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service058Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
