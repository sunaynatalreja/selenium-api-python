# import pytest
# import allure
#
# from src.web.pages.product_page import ProductPage
#
#
# @pytest.mark.usefixtures("setup")
# class TestHomePage:
#     @allure.title("Buy Product Flow")
#     @allure.description('''
#     Scenario: Successful product purchase
#
#     GIVEN a user is logged into the application
#     AND user is on the product listing page
#     AND a product is available in stock
#
#     WHEN a user selects the product
#     AND user adds it to the cart
#     AND user proceeds to checkout
#     AND user enters valid shipping and payment details
#     AND user confirms the order
#
#     THEN order should be placed successfully
#     AND user should see an order confirmation message
#     AND order details should appear in the user’s order history
#     AND inventory count should be reduced by one
#
#     ''')
#     def test_buy_flow(self):
#         product_page = ProductPage(self.driver)
#         product_page.open()
#         assert("STORE" in product_page.get_page_title())