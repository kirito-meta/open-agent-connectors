"""
Unit tests for Service051 Connector.
"""

import pytest
from service_051.connector import Service051Connector

def test_connection_success():
    connector = Service051Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service051Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
