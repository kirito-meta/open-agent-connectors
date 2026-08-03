"""
Unit tests for Service036 Connector.
"""

import pytest
from service_036.connector import Service036Connector

def test_connection_success():
    connector = Service036Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service036Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
