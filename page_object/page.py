from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.todo_row import ToDoRow

class Page:
    __url = 'https://sky-todo-list.herokuapp.com'
    
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        
    def open(self):
        self.__driver.get(self.__url)
        return self
    
    def get_todos(self) -> list[ToDoRow]:
        rows = self.__driver.find_elements(By.CSS_SELECTOR, "td")
        todos = []
        for row in rows:
            new_row = ToDoRow(row)
            todos.append(new_row)
        return todos
        