"""
Unit tests for Service018 Connector.
"""

import pytest
from service_018.connector import Service018Connector

def test_connection_success():
    connector = Service018Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service018Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
