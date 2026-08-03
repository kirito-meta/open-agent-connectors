"""
Unit tests for Service081 Connector.
"""

import pytest
from service_081.connector import Service081Connector

def test_connection_success():
    connector = Service081Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service081Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
