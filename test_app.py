import json

import pytest

from app import create_app


PORT = 5007


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    # db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    # app = create_app({"TESTING": True, "DATABASE": db_path})
    app = create_app()

    # create the database and load test data
    #with app.app_context():
    #    init_db()
    #    get_db().executescript(_data_sql)

    yield app

    # close and remove the temporary database
    #os.close(db_fd)
    #os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_index_endpoint_status(client):
    response = client.get("/")
    assert response.status_code == 200


def test_lookup_endpoint_status(client):
    response = client.get("/lookup")
    assert response.status_code == 302


def test_lookup_word_none(client):
    """Test lookup redirects to self if word is None"""
    response = client.get("/lookup", follow_redirects=True)
    assert b"etymology index" in response.data


@pytest.mark.skip(reason="Is hitting 3rd party pages.")
def test_lookup_word_redirect(client):
    """Test GET request for lookup word redirects to results"""
    response = client.get("/lookup?word=bear")
    assert b"etymology result" in response.data


@pytest.mark.skip(reason="Is hitting 3rd party pages.")
def test_lookup_word_write_to_all(client):
    """Test GET request for lookup word. """
    def get_num_searches():
        return len(json.loads(client.get("/all").data))
    num_searches = get_num_searches()
    response = client.get("/lookup?word=hamster")
    assert get_num_searches() == num_searches + 1


def test_lookup_all_status(client):
    response = client.get("/all")
    assert response.status_code == 200
