import requests

class ToDoService:
    
    def __init__(self) -> None:
        self.__url = "https://todo-app-sky.herokuapp.com/"
        
    def create_todo(self, title: str) -> dict:
        body = { "title": title , "completed": False }
        response = requests.post(self.__url, json=body)
        return response.json()
  