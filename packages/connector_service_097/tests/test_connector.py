"""
Unit tests for Service097 Connector.
"""

import pytest
from service_097.connector import Service097Connector

def test_connection_success():
    connector = Service097Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service097Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
