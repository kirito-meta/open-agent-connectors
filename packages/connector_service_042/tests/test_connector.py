"""
Unit tests for Service042 Connector.
"""

import pytest
from service_042.connector import Service042Connector

def test_connection_success():
    connector = Service042Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service042Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
