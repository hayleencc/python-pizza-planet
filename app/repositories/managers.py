from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column

from .models import Beverage, BeverageDetail, Ingredient, Order, OrderDetail, Size, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)

    @classmethod
    def drop(cls):
        cls.session.query(cls.model).delete()
        cls.session.commit()


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((OrderDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.add_all((BeverageDetail(order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')

    @classmethod
    def drop(cls):
        cls.session.query(OrderDetail).delete()
        cls.session.query(BeverageDetail).delete()
        cls.session.commit()
        super().drop()


class ReportManager(BaseManager):

    @classmethod
    def get_most_requested_ingredient(cls):
        most_requested_ingredient_result = cls.session.query(Ingredient.name,
                                                             db.func.sum(OrderDetail.ingredient_price).label(
                                                                 'total price'),
                                                             db.func.count(OrderDetail.ingredient_id).label(
                                                                 'count')
                                                             ).join(OrderDetail, OrderDetail.ingredient_id == Ingredient._id).group_by(Ingredient._id).order_by(db.func.count(OrderDetail.ingredient_id).desc()).all()

        most_requested_ingredient = most_requested_ingredient_result[0][0]
        most_requested_ingredient_price = round(
            most_requested_ingredient_result[0][1], 2)
        most_requested_ingredient_count = most_requested_ingredient_result[0][2]
        return {
            'name': most_requested_ingredient,
            'total_price': most_requested_ingredient_price,
            'count': most_requested_ingredient_count
        }

    @classmethod
    def get_month_with_more_revenue(cls):
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
        month_with_more_revenue_result = cls.session.query(db.func.extract('month', Order.date).label('month'),
                                                           db.func.sum(Order.total_price).label(
            'total price')
        ).group_by(db.func.extract('month', Order.date)).order_by(db.func.sum(Order.total_price).desc()).all()

        month_with_more_revenue = int(month_with_more_revenue_result[0][0])
        total_price_month_with_more_revenue = round(
            month_with_more_revenue_result[0][1], 2)
        return {
            'month': months[month_with_more_revenue-1],
            'total_price': total_price_month_with_more_revenue
        }

    @classmethod
    def get_top_three_customers(cls):
        top_three_customers = cls.session.query(Order.client_name,
                                                db.func.sum(Order.total_price).label(
                                                    'total_purchases')
                                                ).group_by(Order.client_dni).order_by(db.func.sum(Order.total_price).desc()).limit(3).all()

        return [{
            'client_name': customer.client_name,
            'total_purchases': round(customer.total_purchases, 2)
        } for customer in top_three_customers]


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
