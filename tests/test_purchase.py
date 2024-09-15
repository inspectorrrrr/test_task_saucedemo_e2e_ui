import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_purchase_flow(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавление товара в корзину
    inventory_page = InventoryPage(driver)
    assert "inventory.html" in driver.current_url, "Ошибка входа в систему, вы не находитесь на странице товаров"

    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    # Переход к оформлению
    cart_page = CartPage(driver)
    assert "cart.html" in driver.current_url, "Вы не находитесь на странице корзина"

    cart_page.proceed_to_checkout()

    # Оформление покупки
    checkout_page = CheckoutPage(driver)
    assert "checkout-step-one.html" in driver.current_url, "Вы не находитесь на странице оформления заказа"

    checkout_page.fill_checkout_info("Qwerty", "Asdfgh", "123456")
    assert "checkout-step-two.html" in driver.current_url, "Вы не находитесь на финальной странице заказа"

    checkout_page.finish_checkout()

    # Проверка успешного завершения
    assert "checkout-complete.html" in driver.current_url, "Покупка не завершена"

    checkout_page.verify_order_completion()
