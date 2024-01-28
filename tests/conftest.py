import pytest
from app import app, db, Transaction

@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client