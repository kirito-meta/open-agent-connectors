"""
Unit tests for Service005 Connector.
"""

import pytest
from service_005.connector import Service005Connector

def test_connection_success():
    connector = Service005Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service005Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
