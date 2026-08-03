"""
Unit tests for Service055 Connector.
"""

import pytest
from service_055.connector import Service055Connector

def test_connection_success():
    connector = Service055Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service055Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
