"""
Unit tests for Service072 Connector.
"""

import pytest
from service_072.connector import Service072Connector

def test_connection_success():
    connector = Service072Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service072Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
