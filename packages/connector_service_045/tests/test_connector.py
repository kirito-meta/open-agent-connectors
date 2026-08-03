"""
Unit tests for Service045 Connector.
"""

import pytest
from service_045.connector import Service045Connector

def test_connection_success():
    connector = Service045Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service045Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
