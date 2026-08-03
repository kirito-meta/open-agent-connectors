"""
Unit tests for Service015 Connector.
"""

import pytest
from service_015.connector import Service015Connector

def test_connection_success():
    connector = Service015Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service015Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
