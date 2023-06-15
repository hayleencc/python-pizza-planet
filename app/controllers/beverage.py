from .base import BaseController
from ..repositories.managers import BeverageManager


class BeverageController(BaseController):
    manager = BeverageManager
