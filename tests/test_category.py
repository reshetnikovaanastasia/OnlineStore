def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3


def test_add_products(first_category, first_product):
    first_category.add_product(first_product)
    assert first_category.products == (f"Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                       f"Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                       f"{first_product.name}, {first_product.price} руб. "
                                       f"Остаток: {first_product.quantity} шт.\n")
