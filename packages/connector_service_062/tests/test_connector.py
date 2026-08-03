"""
Unit tests for Service062 Connector.
"""

import pytest
from service_062.connector import Service062Connector

def test_connection_success():
    connector = Service062Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service062Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
