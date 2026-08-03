"""
Unit tests for Service025 Connector.
"""

import pytest
from service_025.connector import Service025Connector

def test_connection_success():
    connector = Service025Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service025Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
