"""
Unit tests for Service022 Connector.
"""

import pytest
from service_022.connector import Service022Connector

def test_connection_success():
    connector = Service022Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service022Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
