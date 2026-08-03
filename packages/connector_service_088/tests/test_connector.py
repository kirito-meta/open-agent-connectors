"""
Unit tests for Service088 Connector.
"""

import pytest
from service_088.connector import Service088Connector

def test_connection_success():
    connector = Service088Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service088Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
