"""
Unit tests for Service030 Connector.
"""

import pytest
from service_030.connector import Service030Connector

def test_connection_success():
    connector = Service030Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service030Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
