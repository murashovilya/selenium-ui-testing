from dataclasses import dataclass, field

from faker import Faker


@dataclass
class Customer:
    first_name: str = field(default_factory=lambda: Faker().first_name())
    last_name: str = field(default_factory=lambda: Faker().last_name())
    post_code: str = field(default_factory=lambda: Faker().postcode())


@dataclass
class Credentials:
    username: str = field(default_factory=lambda: Faker().user_name())
    password: str = field(default_factory=lambda: Faker().password())
