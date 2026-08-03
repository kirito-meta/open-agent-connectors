"""
Unit tests for Service009 Connector.
"""

import pytest
from service_009.connector import Service009Connector

def test_connection_success():
    connector = Service009Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service009Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
