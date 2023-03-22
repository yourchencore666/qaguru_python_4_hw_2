import pytest

from tests.models.users_examples import Worker, UserStatus, CsvUserProvider, ApiUserProvider


@pytest.fixture(params=[CsvUserProvider, ApiUserProvider])
def user_provider():
   return CsvUserProvider('../users.csv')

@pytest.fixture()
def users(user_provider):
    users = user_provider.get_users()
    return users
    # class_users = []
    # for user in users:
    #     class_users.append(User.from_csv_user(user))

@pytest.fixture()
def workers(users):
    workers = [Worker.from_user(user) for user in users if user.status == UserStatus.worker]
    return workers


def test_workers_are_adults(workers):
    for worker in workers:
        assert worker.is_adult()
