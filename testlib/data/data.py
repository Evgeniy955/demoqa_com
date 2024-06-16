from dataclasses import dataclass


@dataclass
class Person:
    last_name: str = None
    first_name: str = None
    email: str = None
    current_address: str = None
    mobile: str = None
    subject: str = None