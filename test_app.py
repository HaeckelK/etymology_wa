"""
Draft functional tests to see that endpoints working etc.

Need to actaully spin up the server.

These can't be used for coverage etc because the codebase isn't being run by the tests.

Intended as a quick litmus test while I put in create_app etc, and can then shift to test_client.
"""
import pytest
import requests

import app


PORT = 5007


def test_index_endpoint_status():
    response = requests.get(f'http://127.0.0.1:{PORT}/')
    assert response.status_code == 200


def test_lookup_endpoint_status():
    response = requests.get(f'http://127.0.0.1:{PORT}/lookup')
    assert response.status_code == 200


def test_lookup_all_status():
    response = requests.get(f'http://127.0.0.1:{PORT}/all')
    assert response.status_code == 200
