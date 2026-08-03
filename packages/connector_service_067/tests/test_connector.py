"""
Unit tests for Service067 Connector.
"""

import pytest
from service_067.connector import Service067Connector

def test_connection_success():
    connector = Service067Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service067Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
