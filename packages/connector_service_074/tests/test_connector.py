"""
Unit tests for Service074 Connector.
"""

import pytest
from service_074.connector import Service074Connector

def test_connection_success():
    connector = Service074Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service074Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
