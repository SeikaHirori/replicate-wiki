
from enum import auto
import pytest
from playwright.sync_api import Page, expect

class Test_create:

    @pytest.fixture(scope="function", autouse=True)
    def setup_create_page(self, page:Page):
        page.goto("http://localhost:8000/create")
        yield

    def test_contains_title(self, page: Page):
        # page.goto("http://localhost:8000/create")
        expect(page).to_have_title("Create")

    def test_contains_url(self, page: Page):
        expect(page).to_have_url("http://localhost:8000/create")
            

class Test_layout:

    @pytest.fixture(scope="function", autouse=True)
    def setup_create_page(self, page: Page):
        page.goto("http://localhost:8000/")

    def test_function_clicking_to_create_page(self, page:Page):
        desired_text:str = "text=Create New Page"

        # Assign variable to store locator info
        attribute_create_new_page = page.locator(desired_text)
        expect(attribute_create_new_page).to_have_attribute("href", " /create ") # Whitespace around the link is needed for Django template variables

        # Now, click on link to move to the page.
        page.locator(desired_text).click()
        expect(page).to_have_url("http://localhost:8000/create")

        