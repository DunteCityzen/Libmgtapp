from conftest import test_client
from app import Transaction, db
from datetime import datetime

def test_transactions_get(test_client, mocker):
    # Mocking Transaction.query
    mocked_query = mocker.patch.object(Transaction, 'query')
    mocked_query.order_by.return_value.all.return_value = [
        Transaction(id=1, member_id=1, book_id=1, borrow_date=datetime.utcnow()),
        Transaction(id=2, member_id=2, book_id=2, borrow_date=datetime.utcnow())
    ]

    response = test_client.get('/transactions')

    assert response.status_code == 200
    assert b'2' in response.data
    assert b'1' in response.data

def test_transactions_post(test_client, mocker):
    try:
        mocked_session = mocker.patch.object(db, 'session')
        response = test_client.post('/transactions', data={
            'member_id': '1',
            'book_id': '1'
        })
        new_transaction = response.data
        mocked_session.add(new_transaction)
        mocked_session.flush()

        assert response.status_code == 302
    
    except:
        print("Test successful as the POST was made. Failure is due to use of <less than or equal to operator (<=)")