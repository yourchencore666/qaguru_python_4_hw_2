"""
Протестируйте классы из модуля homework/shop_models.py
"""
import pytest

from models.shop_models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product2():
    return Product("pen", 200.0, "This is a pen", 500)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1001) == False
        assert product.check_quantity(1000) == True
        assert product.check_quantity(999) == True
        assert product.check_quantity(0) == True
        assert product.check_quantity(-1) == True


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(0) == 1000
        assert product.buy(1) == 999
        assert product.buy(999) == 0



    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        assert product.buy(1001) == (ValueError, "Количества продуктов не хватает")

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product_in_cart(self, product):
        cart = Cart()
        cart.add_product(product, 1)
        assert cart.products == {product: 1}


    def test_add_product_in_cart_iteration(self, product):
            cart = Cart()
            cart.add_product(product, 1)
            cart.add_product(product, 1)
            assert cart.products == {product: 2}


    def test_add_product_in_cart_with_invalid_value(self, product):
        cart = Cart()
        with pytest.raises(ValueError, match="Количество товара должно быть целым положительным числом"):
            cart.add_product(product, -1)

    def test_remove_product_without_quantity(self, product):
        cart = Cart()
        cart.products = {product: 3}
        cart.remove_product(product)
        assert cart.products == {}

    def test_remove_product_with_quantity(self, product):
        cart = Cart()
        cart.products = {product: 300}
        cart.remove_product(product, 200)
        assert cart.products == {product: 100}


    def test_remove_product_with_more_than_quantity(self, product):
        cart = Cart()
        cart.products = {product: 200}
        cart.remove_product(product, 300)
        assert cart.products == {}


    def test_remove_product_with_equal_quantity(self, product):
        cart = Cart()
        cart.products = {product: 200}
        cart.remove_product(product, 200)
        assert cart.products == {}


    def test_clear_cart(self, product):
        cart = Cart()
        cart.products = {product: 200}
        cart.clear()
        assert cart.products == {}


    def test_clear_empty_cart(self):
        cart = Cart()
        cart.products = {}
        cart.clear()
        assert cart.products == {}


    def test_get_total_price(self, product, product2):
        cart = Cart()
        cart.products = {product: 200, product2: 300}
        total_price = cart.get_total_price()
        assert total_price == product.price * 200 + product2.price * 300

    def test_buy(self, product, product2):
        cart = Cart()
        final_quantity_first_product = product.quantity - 900
        final_quantity_second_product = product2.quantity - 400

        cart.products = {product: 900, product2: 400}
        cart.buy()
        assert product.quantity == final_quantity_first_product
        assert product2.quantity == final_quantity_second_product
        assert cart.products == {}

    def test_buy_more_than_available(self, product, product2):
        cart = Cart()
        cart.products = {product: 1000, product2: 501}
        assert product.quantity == 1000
        with pytest.raises(ValueError, match="Товара не хватает на складе"):
            cart.buy()