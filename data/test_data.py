from dataclasses import dataclass, field

from faker import Faker


@dataclass
class Customer:
    first_name: str = field(default_factory=lambda: Faker().first_name())
    last_name: str = field(default_factory=lambda: Faker().last_name())
    email: str = field(default_factory=lambda: Faker().email())
    phone_number: str = field(default_factory=lambda: Faker().phone_number())


@dataclass
class Credentials:
    username: str = field(default_factory=lambda: Faker().user_name())
    password: str = field(default_factory=lambda: Faker().password())
