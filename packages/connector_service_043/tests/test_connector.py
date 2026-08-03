"""
Unit tests for Service043 Connector.
"""

import pytest
from service_043.connector import Service043Connector

def test_connection_success():
    connector = Service043Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service043Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
