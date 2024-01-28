from conftest import test_client
from app import Member, db

def test_index_get(test_client, mocker):
    # Mocking Member.query
    mocked_query = mocker.patch.object(Member, 'query')
    mocked_query.order_by.return_value.all.return_value = [
        Member(id=1, name='Member name 1', debt=0),
        Member(id=2, name='Member name 2', debt=0)
    ]

    response = test_client.get('/members')

    assert response.status_code == 200
    assert b'Member name 1' in response.data
    assert b'Member name 2' in response.data

def test_members_post(test_client, mocker):
    mocked_session = mocker.patch.object(db, 'session')
    response = test_client.post('/members', data={
        'name': 'Testname'
    })
    new_member = response.data
    mocked_session.add(new_member)
    mocked_session.flush()

    assert response.status_code == 302