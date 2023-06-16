from ..controllers import BeverageController
from app.services.BaseBlueprint import BaseBlueprint

beverage = BaseBlueprint('beverage', __name__, BeverageController)
