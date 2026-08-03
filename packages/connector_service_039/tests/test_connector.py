"""
Unit tests for Service039 Connector.
"""

import pytest
from service_039.connector import Service039Connector

def test_connection_success():
    connector = Service039Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service039Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
