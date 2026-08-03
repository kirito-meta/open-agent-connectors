"""
Unit tests for Service090 Connector.
"""

import pytest
from service_090.connector import Service090Connector

def test_connection_success():
    connector = Service090Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service090Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
