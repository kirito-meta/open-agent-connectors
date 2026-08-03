"""
Unit tests for Service027 Connector.
"""

import pytest
from service_027.connector import Service027Connector

def test_connection_success():
    connector = Service027Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service027Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
