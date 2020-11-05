"""
Draft functional tests to see that endpoints working etc.

Need to actaully spin up the server.

These can't be used for coverage etc because the codebase isn't being run by the tests.

Intended as a quick litmus test while I put in create_app etc, and can then shift to test_client.
"""
import json

import pytest
import requests


PORT = 5007


def test_index_endpoint_status():
    response = requests.get(f'http://127.0.0.1:{PORT}/')
    assert response.status_code == 200


def test_lookup_endpoint_status():
    response = requests.get(f'http://127.0.0.1:{PORT}/lookup')
    assert response.status_code == 200


def test_lookup_word_none():
    """Test lookup redirects to self if word is None"""
    response = requests.get(f'http://127.0.0.1:{PORT}/lookup')
    assert "etymology index" in response.text


@pytest.mark.skip(reason="Is hitting 3rd party pages.")
def test_lookup_word_redirect():
    """Test GET request for lookup word redirects to results"""
    response = requests.get(f'http://127.0.0.1:{PORT}/lookup?word=bear')
    assert "etymology result" in response.text


@pytest.mark.skip(reason="Is hitting 3rd party pages.")
def test_lookup_word_write_to_all():
    """Test GET request for lookup word. """
    def get_num_searches():
        return len(json.loads(requests.get(f'http://127.0.0.1:{PORT}/all').content))
    num_searches = get_num_searches()
    response = requests.get(f'http://127.0.0.1:{PORT}/lookup?word=hamster')
    assert get_num_searches() == num_searches + 1


def test_lookup_all_status():
    response = requests.get(f'http://127.0.0.1:{PORT}/all')
    assert response.status_code == 200
