"""
Unit tests for Service026 Connector.
"""

import pytest
from service_026.connector import Service026Connector

def test_connection_success():
    connector = Service026Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service026Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
