"""
Unit tests for Service028 Connector.
"""

import pytest
from service_028.connector import Service028Connector

def test_connection_success():
    connector = Service028Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service028Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
