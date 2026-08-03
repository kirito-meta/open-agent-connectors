"""
Unit tests for Service032 Connector.
"""

import pytest
from service_032.connector import Service032Connector

def test_connection_success():
    connector = Service032Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service032Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
