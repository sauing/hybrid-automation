from playwright.sync_api import Page, expect
from .base_page import BasePage

class InventoryPage(BasePage):
    # Example selectors for an inventory/products page. Replace with your application's selectors.
    inventory_container = ".inventory_list"
    add_to_cart_btn = "button[data-test='add-to-cart-sauce-labs-backpack']"
    cart_icon = ".shopping_cart_link"

    def __init__(self, page: Page) -> None:
        """
        Example InventoryPage object. Replace selectors and methods as needed for your app.
        Extend this class for your own inventory/product workflows.
        """
        super().__init__(page)

    def should_be_visible(self) -> None:
        """
        Assert that the inventory container is visible on the page.

        Returns:
            None
        """
        expect(self.page.locator(self.inventory_container)).to_be_visible()

    def add_backpack_to_cart(self) -> None:
        """
        Click the 'Add to cart' button for the backpack item.

        Returns:
            None
        """
        self.page.click(self.add_to_cart_btn)

    def open_cart(self) -> None:
        """
        Click the cart icon to open the shopping cart.

        Returns:
            None
        """
        self.page.click(self.cart_icon)

# Example usage:
# class MyInventoryPage(InventoryPage):
#     ...
