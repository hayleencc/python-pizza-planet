import pytest
from app.controllers.report import ReportController


def test_get_report():
    report, error = ReportController.get_report()
    pytest.assume(error is None)
    pytest.assume(report['month_with_more_revenue'])
    pytest.assume(report['most_requested_ingredient'])
    pytest.assume(report['top_three_customers'])
