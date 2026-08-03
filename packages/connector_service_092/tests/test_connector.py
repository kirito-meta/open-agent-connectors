"""
Unit tests for Service092 Connector.
"""

import pytest
from service_092.connector import Service092Connector

def test_connection_success():
    connector = Service092Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service092Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
