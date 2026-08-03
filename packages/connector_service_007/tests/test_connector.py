"""
Unit tests for Service007 Connector.
"""

import pytest
from service_007.connector import Service007Connector

def test_connection_success():
    connector = Service007Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service007Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
