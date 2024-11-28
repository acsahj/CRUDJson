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
    def load_list(self):
        # base_path = "/Users/acsah/technicalTester"
        # file_path = "base_path/gitPractice/src/todos.json"
        try: 
            with open(file_path,"r") as file:
                data=json.load(file)
                print("To dos from JSON file:",data)
            return data
        except FileNotFoundError:
         print(f"Error: The file at {file_path}was not found")

        except json.JSONDecodeError:
            print(f"Error:The file at {file_path} contains invalid JSON")
    
        except Exception as e:
            print("An unexpected error occurred : {e}")
        return []
toDo = jsonWork()
toDo.load_list()


    

