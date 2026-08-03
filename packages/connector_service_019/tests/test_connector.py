"""
Unit tests for Service019 Connector.
"""

import pytest
from service_019.connector import Service019Connector

def test_connection_success():
    connector = Service019Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service019Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
