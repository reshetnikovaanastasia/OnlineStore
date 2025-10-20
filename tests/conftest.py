import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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


@pytest.fixture
def third_product():
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8)


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


@pytest.fixture
def first_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                      5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def second_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                      98.2, "15", 512, "Gray space")


@pytest.fixture
def first_LawnGrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture
def second_LawnGrass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                     "США", "5 дней", "Темно-зеленый")
