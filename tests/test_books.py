from conftest import test_client
from app import Book, db

def test_index_get(test_client, mocker):
    # Mocking Book.query
    mocked_query = mocker.patch.object(Book, 'query')
    mocked_query.order_by.return_value.all.return_value = [
        Book(id=1, title='Book 1', author='Author 1'),
        Book(id=2, title='Book 2', author='Author 2')
    ]

    response = test_client.get('/')

    assert response.status_code == 200
    assert b'Book 1' in response.data
    assert b'Book 2' in response.data

def test_index_post(test_client, mocker):
    mocked_session = mocker.patch.object(db, 'session')
    response = test_client.post('/', data={
        'title': 'Testbook',
        'author': 'Testauthor'
    })
    new_book = response.data
    mocked_session.add(new_book)
    mocked_session.flush()

    assert response.status_code == 302

