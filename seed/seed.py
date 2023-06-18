from app.controllers.order import OrderController
from app.repositories.managers import BeverageManager, IngredientManager, OrderManager, SizeManager
from .seed_utils.seed_utils import generate_client_mock, generate_item_mock, get_random_item, get_random_items_list, get_random_date
from .seed_utils.seed_constants import beverages, ingredients, sizes


class DatabaseSeeder:
    def __init__(self):
        self.orders = []
        self.ingredients = []
        self.sizes = []
        self.beverages = []
        self.clients = []
        self.OrderController = OrderController()
        self.OrderManager = OrderManager()
        self.IngredientManager = IngredientManager()
        self.SizeManager = SizeManager()
        self.BeverageManager = BeverageManager()

    def seed(self):
        self.seed_ingredients()
        self.seed_beverages()
        self.seed_sizes()
        self.seed_orders()

    def seed_ingredients(self):
        for ingredient in ingredients:
            self.ingredients.append(self.IngredientManager.create(
                generate_item_mock(ingredient))["_id"])

    def seed_beverages(self):
        for beverage in beverages:
            self.beverages.append(self.BeverageManager.create(
                generate_item_mock(beverage))["_id"])

    def seed_sizes(self):
        for size in sizes:
            self.sizes.append(self.SizeManager.create(
                generate_item_mock(size))["_id"])

    def seed_orders(self):
        for _ in range(100):
            client = generate_client_mock()
            size = get_random_item(self.sizes)
            order_ingredients = get_random_items_list(self.ingredients)
            order_beverages = get_random_items_list(self.beverages)
            self.orders.append(self.OrderController.create({
                'client_name': client['client_name'],
                'client_dni': client['client_dni'],
                'client_address': client['client_address'],
                'client_phone': client['client_phone'],
                'date': get_random_date(),
                'size_id': size,
                'ingredients': order_ingredients,
                'beverages': order_beverages
            }))

    def drop_tables(self):
        self.OrderManager.drop()
        self.IngredientManager.drop()
        self.SizeManager.drop()
        self.BeverageManager.drop()


Seeder = DatabaseSeeder()
