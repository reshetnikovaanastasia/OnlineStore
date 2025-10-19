class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Неверный ввод, ожидался Product")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, params_dict):
        """Добавление нового продукта"""
        return cls(**params_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        """Изменение цены"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price
