"""
Unit tests for Service060 Connector.
"""

import pytest
from service_060.connector import Service060Connector

def test_connection_success():
    connector = Service060Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service060Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
