from src.product import Product


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
