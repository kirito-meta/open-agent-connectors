"""
Unit tests for Service046 Connector.
"""

import pytest
from service_046.connector import Service046Connector

def test_connection_success():
    connector = Service046Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service046Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
