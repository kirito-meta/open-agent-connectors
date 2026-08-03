"""
Unit tests for Service061 Connector.
"""

import pytest
from service_061.connector import Service061Connector

def test_connection_success():
    connector = Service061Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service061Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
