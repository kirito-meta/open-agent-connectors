"""
Unit tests for Service086 Connector.
"""

import pytest
from service_086.connector import Service086Connector

def test_connection_success():
    connector = Service086Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service086Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
