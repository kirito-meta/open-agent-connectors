"""
Unit tests for Service002 Connector.
"""

import pytest
from service_002.connector import Service002Connector

def test_connection_success():
    connector = Service002Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service002Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
