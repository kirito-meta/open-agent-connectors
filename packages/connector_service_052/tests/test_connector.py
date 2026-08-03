"""
Unit tests for Service052 Connector.
"""

import pytest
from service_052.connector import Service052Connector

def test_connection_success():
    connector = Service052Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service052Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
