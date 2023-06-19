from datetime import datetime, timedelta
from faker import Faker
import random
fake = Faker()


def generate_random_price() -> float:
    return round(random.uniform(1, 10), 2)

def generate_item_mock(item: str) -> dict:
    return {
        'name': item, 'price': generate_random_price()
    }


def get_random_item(items: list) -> str:
    return random.choice(items)


def get_random_client() -> dict:
    return get_random_item(mocked_clients)


def get_random_items_list(items: list) -> list:
    items_count = random.randint(1, len(items))
    return random.sample(items, items_count)


def get_random_date() -> str:
    current_datetime = datetime.now()
    last_year_datetime = current_datetime - timedelta(days=365)
    random_timedelta = timedelta(seconds=random.randint(
        0, int((current_datetime - last_year_datetime).total_seconds())))
    random_datetime = last_year_datetime + random_timedelta
    return random_datetime


def generate_clients_name() -> list:
    mocked_clients = []
    for _ in range(10):
        mocked_clients.append(generate_client_mock())
    return mocked_clients


def generate_client_mock() -> dict:
    return {
        'client_name': fake.name(),
        'client_dni': fake.random_number(digits=10),
        'client_address': fake.address(),
        'client_phone': fake.phone_number(),
    }


mocked_clients: list = generate_clients_name()
