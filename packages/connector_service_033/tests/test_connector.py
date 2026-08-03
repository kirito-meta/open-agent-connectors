"""
Unit tests for Service033 Connector.
"""

import pytest
from service_033.connector import Service033Connector

def test_connection_success():
    connector = Service033Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service033Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
