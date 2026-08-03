"""
Unit tests for Service098 Connector.
"""

import pytest
from service_098.connector import Service098Connector

def test_connection_success():
    connector = Service098Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service098Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
