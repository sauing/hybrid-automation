import requests
from src.utils.config import CFG
from src.utils.logger import log

class ApiClient:
    def __init__(self, token: str | None = None) -> None:
        """
        Initialize the ApiClient.

        Args:
            token (str | None, optional): Bearer token for authentication. Defaults to None.

        Returns:
            None
        """
        self.base = CFG["api_base"].rstrip("/")
        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get_products(self) -> requests.Response:
        """
        Retrieve the list of products from the API.

        Returns:
            requests.Response: The HTTP response object containing the products list.
        """
        url = f"{self.base}/products"
        log.info(f"GET {url}")
        return self.session.get(url, timeout=30)

    def get_product(self, product_id: int) -> requests.Response:
        """
        Retrieve a single product by its ID from the API.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            requests.Response: The HTTP response object containing the product details.
        """
        url = f"{self.base}/products/{product_id}"
        log.info(f"GET {url}")
        return self.session.get(url, timeout=30)
