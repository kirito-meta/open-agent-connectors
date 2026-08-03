"""
Unit tests for Service080 Connector.
"""

import pytest
from service_080.connector import Service080Connector

def test_connection_success():
    connector = Service080Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service080Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
