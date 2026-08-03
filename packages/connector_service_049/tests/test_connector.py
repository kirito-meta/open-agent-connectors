"""
Unit tests for Service049 Connector.
"""

import pytest
from service_049.connector import Service049Connector

def test_connection_success():
    connector = Service049Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service049Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
