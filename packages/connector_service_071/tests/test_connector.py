"""
Unit tests for Service071 Connector.
"""

import pytest
from service_071.connector import Service071Connector

def test_connection_success():
    connector = Service071Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service071Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
