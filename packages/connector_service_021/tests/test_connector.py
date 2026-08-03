"""
Unit tests for Service021 Connector.
"""

import pytest
from service_021.connector import Service021Connector

def test_connection_success():
    connector = Service021Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service021Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
