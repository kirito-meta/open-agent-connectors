"""
Unit tests for Service100 Connector.
"""

import pytest
from service_100.connector import Service100Connector

def test_connection_success():
    connector = Service100Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service100Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
