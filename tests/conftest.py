import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


@pytest.fixture
def second_product():
    return {"name": "Samsung Galaxy S24 Ultra",
            "description": "257GB, Серый цвет, 201MP камера", "price": 180001.0,
            "quantity": 6}


@pytest.fixture()
def first_category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [Product("Iphone 15",
                             "512GB, Gray space",
                             210000.0,
                             8), Product("Samsung Galaxy S23 Ultra",
                                         "256GB, Серый цвет, 200MP камера",
                                         180000.0,
                                         5)])


@pytest.fixture()
def second_category():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
                    [Product("55\" QLED 4K",
                             "Фоновая подсветка",
                             123000.0,
                             7)])
