"""
Unit tests for Service031 Connector.
"""

import pytest
from service_031.connector import Service031Connector

def test_connection_success():
    connector = Service031Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service031Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
