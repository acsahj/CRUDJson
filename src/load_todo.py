'''
1 Load Todos
Function: load_list
Description: Load the list of todos from a JSON file.
Details:
Use a hardcoded file path (e.g., "data/todos.json").
If the file is missing, the function should return an empty list and log a warning message.
If there's an error reading or parsing the JSON file, log the error and handle it gracefully.
'''

import json
import logging
import uuid
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TodoNotFoundError(Exception):
    """Exception raised when a todo with specified ID is not found."""
    pass

class TodoManager:
    # Use a hardcoded file path
    file_path = "data/todos.json"
    
    @classmethod
    def load_list(cls):
        """
        Load the list of todos from a JSON file.
        Returns an empty list if the file is missing or contains invalid JSON.
        """
        try: 
            with open(cls.file_path, "r") as file:
                data = json.load(file)
                # Extract todos from the 'todo' key in the JSON structure
                todos = data.get("todo", [])
                logger.info(f"Successfully loaded {len(todos)} todos from {cls.file_path}")
                return todos
        except FileNotFoundError:
            logger.warning(f"Warning: The file at {cls.file_path} was not found. Returning empty list.")
            return []
        except json.JSONDecodeError:
            logger.error(f"Error: The file at {cls.file_path} contains invalid JSON. Returning empty list.")
            return []
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}. Returning empty list.")
            return []
    
    @classmethod
    def get_todo_details(cls, todo_id):
        """
        Retrieve details for a specific todo based on a unique identifier.
        Raises TodoNotFoundError if the todo with the given ID doesn't exist.
        """
        try:
            todos = cls.load_list()
            for todo in todos:
                if todo.get("id") == todo_id:
                    logger.info(f"Found todo with ID {todo_id}")
                    return todo
            
            # If we get here, the todo wasn't found
            logger.warning(f"Todo with ID {todo_id} not found")
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
            
        except Exception as e:
            logger.error(f"An unexpected error occurred in get_todo_details: {e}")
            raise
    
    @classmethod
    def save_list(cls, todo_list):
        """
        Save the current list of todos back to the JSON file.
        Maintains the JSON structure with todos in the 'todo' key.
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(cls.file_path), exist_ok=True)
            
            # Prepare data with the correct structure
            data = {"todo": todo_list}
            
            with open(cls.file_path, "w") as file:
                json.dump(data, file, indent=4)
            logger.info(f"Successfully saved {len(todo_list)} todos to {cls.file_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving todos to {cls.file_path}: {e}")
            raise
    
    @classmethod
    def remove_todo(cls, todo_id):
        """
        Remove a todo item from the list by its todo_id.
        Raises TodoNotFoundError if the todo with the given ID doesn't exist.
        """
        todos = cls.load_list()
        for i, todo in enumerate(todos):
            if todo.get("id") == todo_id:
                del todos[i]
                cls.save_list(todos)
                logger.info(f"Successfully removed todo with ID {todo_id}")
                return True
        
        logger.warning(f"Todo with ID {todo_id} not found for removal")
        raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
    
    @classmethod
    def update_todo(cls, todo_id, updated_todo):
        """
        Update an existing todo item with new data.
        Only updates the provided fields in the todo dictionary.
        Raises TodoNotFoundError if the todo with the given ID doesn't exist.
        """
        todos = cls.load_list()
        for i, todo in enumerate(todos):
            if todo.get("id") == todo_id:
                # Update only the provided fields
                for key, value in updated_todo.items():
                    if key != "id":  # Don't allow changing the ID
                        todo[key] = value
                
                cls.save_list(todos)
                logger.info(f"Successfully updated todo with ID {todo_id}")
                return todo
        
        logger.warning(f"Todo with ID {todo_id} not found for update")
        raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
    
    @staticmethod
    def generate_id():
        """
        Generate a new unique identifier (UUID) for each todo item.
        Returns the ID as a hex string.
        """
        return uuid.uuid4().hex

# Example usage (commented out for production)
# try:
#     print(jsonWork.load_list())
#     print(jsonWork.get_todo_details("8af52e54045b423aabaa9bcf7003ff4d"))
# except TodoNotFoundError as e:
#     print(f"Not found: {e}")