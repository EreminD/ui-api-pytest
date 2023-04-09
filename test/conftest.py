import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from api_methods.todo_service import ToDoService

@pytest.fixture()
def driver() -> WebDriver:
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    
    driver.quit()

@pytest.fixture()
def random_todo():
    api = ToDoService()
    api.create_todo("todo from fixture") # Faker
