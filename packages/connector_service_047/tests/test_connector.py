"""
Unit tests for Service047 Connector.
"""

import pytest
from service_047.connector import Service047Connector

def test_connection_success():
    connector = Service047Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service047Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
