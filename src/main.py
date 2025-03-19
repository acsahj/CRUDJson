from load_todo import TodoManager

def main():
    # Load existing todos
    todos = TodoManager.load_list()
    print("Current todos:")
    for todo in todos:
        print(f"ID: {todo['id']}, Title: {todo['title']}, Description: {todo['description']}")

    # Example of adding a new todo
    new_todos = todos + [{
        "id": len(todos) + 1,
        "title": "New Task",
        "description": "This is a new example task",
        "doneStatus": "False"
    }]
    TodoManager.save_list(new_todos)
    
    # Reload and show updated list
    updated_todos = TodoManager.load_list()
    print("\nUpdated todos:")
    for todo in updated_todos:
        print(f"ID: {todo['id']}, Title: {todo['title']}, Description: {todo['description']}")

if __name__ == "__main__":
    main()