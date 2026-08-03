"""
Unit tests for Service065 Connector.
"""

import pytest
from service_065.connector import Service065Connector

def test_connection_success():
    connector = Service065Connector(api_key="test_key")
    assert connector.connect() is True

def test_query_execution():
    connector = Service065Connector(api_key="test_key")
    connector.connect()
    res = connector.execute_query("SELECT 1")
    assert res["status"] == "success"
