from conftest import test_client
from app import Transaction, db

def test_update_transaction(test_client, mocker):
    mocked_session = mocker.patch.object(db, 'session')
    mocked_transaction_query = mocker.patch.object(Transaction, 'query')
    response = test_client.get('/transactions/1/update')
    transaction_to_update = mocked_transaction_query.get_or_404(1)
    mocked_session.update(transaction_to_update)
    mocked_session.flush()

    assert response.status_code == 302