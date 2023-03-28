import csv
import os.path
from dataclasses import dataclass
from enum import Enum


class UserStatus(Enum):
    worker = 'worker'
    student = 'student'

@dataclass
class User:
    name: str
    age: int
    status: UserStatus
    items: list[str]


    def is_adult(self):
        return self.age >= 18


    def get_items_lenght(self):
        return len(self.items)


    @classmethod
    def from_csv_user(cls, user: dict):
       return cls(name=user['name'],
                  age=int(user['age']),
                  status=UserStatus(user['status']),
                  items=user['items'].split(','))


class Worker(User):
    status = UserStatus.worker

    def do_work(self):
        print('Im working')

    @classmethod
    def from_user(cls, user: User):
        assert user.status == cls.status, "Воркера можно создать только из пользователя с типом worker"
        return cls(name=user.name,
            age=user.age,
            status=cls.status,
            items=user.items)


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError

class CsvUserProvider(UserProvider):
    csv_path = str

    def __init__(self, csv_path):
        assert os.path.exists(csv_path)
        self.csv_path = csv_path
    def get_users(self) -> list[User]:
        with open(self.csv_path, 'r') as file:
            users = list(csv.DictReader(file, delimiter=';'))
        class_users = [User.from_csv_user(user) for user in users]
        return class_users

class ApiUserProvider(UserProvider):
    pass

class DataBaseUserProvider(UserProvider):
    pass