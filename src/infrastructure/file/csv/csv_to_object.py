from dataclasses import dataclass

from dataclass_csv import DataclassReader


@dataclass
class User:
    firstname: str
    email: str
    age: int


def csv_to_object():
    with open('sample.csv') as users_csv:
        reader = DataclassReader(users_csv, User)
        csv_list = [User(**x.__dict__) for x in reader]
    return csv_list
