"""
Unit tests for Service010 Connector.
"""

import pytest
from service_010.connector import Service010Connector

def test_connection_success():
    connector = Service010Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service010Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
