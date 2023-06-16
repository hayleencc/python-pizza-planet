from ..controllers import IngredientController
from app.services.BaseBlueprint import BaseBlueprint

ingredient = BaseBlueprint('ingredient', __name__, IngredientController)
