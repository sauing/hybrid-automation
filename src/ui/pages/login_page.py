from playwright.sync_api import Page
from .base_page import BasePage

class LoginPage(BasePage):
    username = "#user-name"
    password = "#password"
    submit = "#login-button"

    def __init__(self, page: Page) -> None:
        """
        Initialize the LoginPage object.

        Args:
            page (Page): The Playwright Page instance to interact with.
        """
        super().__init__(page)

    def login(self, username: str, password: str) -> None:
        """
        Perform login action by filling in the username and password fields and clicking the submit button.

        Args:
            username (str): The username to input.
            password (str): The password to input.

        Returns:
            None
        """
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.submit)
