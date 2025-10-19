from src.product import Product


class Category():
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавление продуктов в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Указан объект с неправильным/недостаточным объёмом характеристик")

    @property
    def products(self):
        """Возвращает список продуктов"""
        # for pr in self.__products:
        #     return f'{Product.name}, {Product.price} руб. Остаток: {Product.quantity} шт.'
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
