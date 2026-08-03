"""
Unit tests for Service029 Connector.
"""

import pytest
from service_029.connector import Service029Connector

def test_connection_success():
    connector = Service029Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service029Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
