import pytest

from src.product import Product
from tests.conftest import first_smartphone, first_LawnGrass, second_LawnGrass


def test_product_init(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_new_product(second_product):
    new = Product.new_product(second_product)
    assert new.name == "Samsung Galaxy S24 Ultra"
    assert new.description == "257GB, Серый цвет, 201MP камера"
    assert new.price == 180001.0
    assert new.quantity == 6


def test_price(second_product):
    new = Product.new_product(second_product)
    new.price = 800
    assert new.price == 800

    new.price = -100
    assert new.price == 800
    new.price = 0
    assert new.price == 800


def test_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add(first_product, third_product):
    assert (first_product + third_product) == 2580000.0


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_LawnGrass_init(first_LawnGrass):
    assert first_LawnGrass.name == "Газонная трава"
    assert first_LawnGrass.description == "Элитная трава для газона"
    assert first_LawnGrass.price == 500.0
    assert first_LawnGrass.quantity == 20
    assert first_LawnGrass.country == "Россия"
    assert first_LawnGrass.germination_period == "7 дней"
    assert first_LawnGrass.color == "Зеленый"


def test_add_similar(first_smartphone, second_smartphone, first_LawnGrass, second_LawnGrass):
    assert first_smartphone + second_smartphone == 2580000.0
    assert first_LawnGrass + second_LawnGrass == 16750.0
    with pytest.raises(TypeError):
        first_smartphone + first_LawnGrass
