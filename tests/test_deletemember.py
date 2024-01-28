from conftest import test_client
from app import Member, db

def test_delete_member(test_client, mocker):
    mocked_query = mocker.patch.object(Member, 'query')
    mocked_session = mocker.patch.object(db, 'session')
    response = test_client.get('/members/1/delete')
    member_to_delete = mocked_query.get_or_404(1)
    mocked_session.delete(member_to_delete)
    mocked_session.flush()

    assert response.status_code == 302