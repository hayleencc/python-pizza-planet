from app.controllers.base import BaseController
from app.repositories.managers import ReportManager


class ReportController(BaseController):
    manager = ReportManager()

    @classmethod
    def get_most_requested_ingredient(cls):
        return cls.manager.get_most_requested_ingredient()

    @classmethod
    def get_month_with_more_revenue(cls):
        return cls.manager.get_month_with_more_revenue()
    
    @classmethod
    def get_top_three_customers(cls):
        return cls.manager.get_top_three_customers()

    @classmethod
    def get_report(cls):
        report = {
            'most_requested_ingredient': cls.get_most_requested_ingredient(),
            'month_with_more_revenue': cls.get_month_with_more_revenue(),
            'top_three_customers': cls.get_top_three_customers()
        }
        return report, None
