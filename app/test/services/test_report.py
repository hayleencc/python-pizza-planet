
import pytest


def test_get_most_requested_ingredient(client, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))


def test_get_month_with_more_revenue(client, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))


def test_get_top_three_customers(client, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
