"""
Unit tests for Service083 Connector.
"""

import pytest
from service_083.connector import Service083Connector

def test_connection_success():
    connector = Service083Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service083Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
