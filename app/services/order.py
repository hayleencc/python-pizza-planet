from ..controllers import OrderController
from app.services.BaseBlueprint import BaseBlueprint

order = BaseBlueprint('order', __name__, OrderController)
