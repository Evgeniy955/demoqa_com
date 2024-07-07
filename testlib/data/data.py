import os
from dataclasses import dataclass


@dataclass
class Person:
    last_name: str = None
    first_name: str = None
    email: str = None
    current_address: str = None
    mobile: str = None
    subject: str = None


@dataclass
class PersonInTextBox:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


def get_project_path():
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
    return path
