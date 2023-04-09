from page_object.page import Page

def delete_first_task_test(driver, random_todo): 
    page = Page(driver).open()
    todos = page.get_todos()
    size_before = len(todos)
    todos[0].delete()
    
    size_after = len(page.get_todos())
    
    assert size_before - size_after == 1
