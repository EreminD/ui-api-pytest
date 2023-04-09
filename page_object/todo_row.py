from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ToDoRow:
    def __init__(self, td: WebElement) -> None:
        self.__row = td.find_element(By.CSS_SELECTOR, 'div')
        
    def delete(self):
        self.__row.find_element(By.CSS_SELECTOR, 'svg[data-icon=trash] path').click()
        sleep(1) # use wait