"""
Unit tests for Service035 Connector.
"""

import pytest
from service_035.connector import Service035Connector

def test_connection_success():
    connector = Service035Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service035Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
