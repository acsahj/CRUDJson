'''
1 Load Todos
Function: load_list
Description: Load the list of todos from a JSON file.
Details:
Use a hardcoded file path (e.g., "data/todos.json").
If the file is missing, the function should return an empty list and log a warning message.
If there’s an error reading or parsing the JSON file, log the error and handle it gracefully.
'''

import json

class jsonWork:
    file_path= "/Users/apple/Documents/CRUDJson/gitPractice/Data/todos.json"
    @classmethod
    def load_list(cls):
        # base_path = "/Users/acsah/technicalTester"
        # file_path = "base_path/gitPractice/src/todos.json"
        try: 
            with open(cls.file_path,"r") as file:
                data=json.load(file)
                #print("To dos from JSON file:",data)
            return data
        except FileNotFoundError:
         print(f"Error: The file at {cls.file_path}was not found")

        except json.JSONDecodeError:
            print(f"Error:The file at {cls.file_path} contains invalid JSON")
    
        except Exception as e:
            print("An unexpected error occurred : {e}")
        return []
    
    @classmethod
    def get_todo_details(cls,todo_id):
        try:
            toDos=cls.load_list()
            toDo_list= toDos.get("todo",[])
            for todo in toDo_list:
                if todo.get("id")==todo_id:
                    print(f"To do details for{todo_id}:{todo} ")
                    return todo
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred in get_todo: {e}")
        return None


    

# jsonWork.load_list()
# jsonWork.get_todo_details(2)