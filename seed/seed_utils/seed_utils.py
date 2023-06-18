from datetime import datetime, timedelta
from faker import Faker
import random
fake = Faker()


def generate_client_mock() -> dict:
    return {
        'client_name': fake.name(),
        'client_dni': fake.random_number(digits=10),
        'client_address': fake.address(),
        'client_phone': fake.phone_number(),
    }


def generate_random_price() -> float:
    return fake.pyfloat(min_value=1, max_value=10, right_digits=2)


def generate_item_mock(item: str) -> dict:
    return {
        'name': item, 'price': generate_random_price()
    }


def get_random_item(items: list) -> str:
    return random.choice(items)


def get_random_items_list(items: list) -> list:
    return random.choices(items, k=random.randint(1, len(items)))


def get_random_date() -> str:
    current_datetime = datetime.now()
    last_year_datetime = current_datetime - timedelta(days=365)
    random_timedelta = timedelta(seconds=random.randint(
        0, int((current_datetime - last_year_datetime).total_seconds())))
    random_datetime = last_year_datetime + random_timedelta
    return random_datetime
