"""
Unit tests for Service006 Connector.
"""

import pytest
from service_006.connector import Service006Connector

def test_connection_success():
    connector = Service006Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service006Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
