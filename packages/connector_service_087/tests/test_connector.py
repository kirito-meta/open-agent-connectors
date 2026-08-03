"""
Unit tests for Service087 Connector.
"""

import pytest
from service_087.connector import Service087Connector

def test_connection_success():
    connector = Service087Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service087Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
