"""
Unit tests for Service068 Connector.
"""

import pytest
from service_068.connector import Service068Connector

def test_connection_success():
    connector = Service068Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service068Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
