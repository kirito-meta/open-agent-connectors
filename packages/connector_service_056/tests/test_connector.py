"""
Unit tests for Service056 Connector.
"""

import pytest
from service_056.connector import Service056Connector

def test_connection_success():
    connector = Service056Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service056Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
