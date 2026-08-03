"""
Unit tests for Service024 Connector.
"""

import pytest
from service_024.connector import Service024Connector

def test_connection_success():
    connector = Service024Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service024Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
