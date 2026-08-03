"""
Unit tests for Service069 Connector.
"""

import pytest
from service_069.connector import Service069Connector

def test_connection_success():
    connector = Service069Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service069Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
