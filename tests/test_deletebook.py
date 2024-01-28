from conftest import test_client
from app import Book, db

def test_delete_book(test_client, mocker):
    mocked_query = mocker.patch.object(Book, 'query')
    mocked_session = mocker.patch.object(db, 'session')
    response = test_client.get('/books/1/delete')
    book_to_delete = mocked_query.get_or_404(1)
    mocked_session.delete(book_to_delete)
    mocked_session.flush()

    assert response.status_code == 302
