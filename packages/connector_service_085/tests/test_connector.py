"""
Unit tests for Service085 Connector.
"""

import pytest
from service_085.connector import Service085Connector

def test_connection_success():
    connector = Service085Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service085Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
