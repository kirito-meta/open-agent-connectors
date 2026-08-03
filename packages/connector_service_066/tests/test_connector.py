"""
Unit tests for Service066 Connector.
"""

import pytest
from service_066.connector import Service066Connector

def test_connection_success():
    connector = Service066Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service066Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
