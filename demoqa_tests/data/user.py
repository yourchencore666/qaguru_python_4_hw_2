import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    gender: str
    phone_number: str


artem = User(first_name='Artem',
             last_name='Yurchenko',
             gender='Male',
             phone_number='1234567890')
