"""
Unit tests for Service014 Connector.
"""

import pytest
from service_014.connector import Service014Connector

def test_connection_success():
    connector = Service014Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service014Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
