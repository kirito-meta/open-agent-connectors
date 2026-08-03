"""
Unit tests for Service082 Connector.
"""

import pytest
from service_082.connector import Service082Connector

def test_connection_success():
    connector = Service082Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service082Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
