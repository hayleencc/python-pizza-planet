import pytest
from app.controllers.report import ReportController


def test_get_most_requested_ingredient(app, mocked_order):
    most_requested_ingredient, error = ReportController.get_most_requested_ingredient()
    pytest.assume(error is None)
    pytest.assume(most_requested_ingredient['_id'] == mocked_order['ingredient_id'])


def test_get_month_with_more_revenue(app, mocked_order):
    month_with_more_revenue, error = ReportController.get_month_with_more_revenue()
    pytest.assume(error is None)
    pytest.assume(month_with_more_revenue['_id'] == mocked_order['month'])

def test_get_top_three_customers(app, mocked_order):
    top_three_customers, error = ReportController.get_top_three_customers()
    pytest.assume(error is None)
    for customer in top_three_customers:
        pytest.assume(customer['_id'] == mocked_order['client_id'])
