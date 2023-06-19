import pytest

from seed.seed import Seeder

@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def create_report(client, report_uri) -> dict:
    response = client.get(report_uri)
    return response
