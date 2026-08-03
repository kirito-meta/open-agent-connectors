"""
Unit tests for Service040 Connector.
"""

import pytest
from service_040.connector import Service040Connector

def test_connection_success():
    connector = Service040Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service040Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
