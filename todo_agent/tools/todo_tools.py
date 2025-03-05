from typing import Dict, List, Optional
from smolagents import tool
from .todo_storage import TodoStorage

# Initialize storage with a fixed path relative to the tools directory
storage = TodoStorage("tools/todo_data.json")

@tool
def add_todo(title: str, description: str = "") -> Dict:
    """Create a new todo item.
    Args:
        title: The title of the todo item
        description: Optional detailed description of the todo item
        
    Returns:
        dict: The newly created todo item with all its properties
    """
    if not title.strip():
        raise ValueError("Title cannot be empty")
    return storage.add_todo(title, description)

@tool
def edit_todo(todo_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Dict:
    """Edit an existing todo item.
    Args:
        todo_id: The unique identifier of the todo to edit
        title: Optional new title for the todo
        description: Optional new description for the todo
        
    Returns:
        dict: The updated todo item
    """
    if not todo_id:
        raise ValueError("Todo ID is required")
        
    updates = {}
    if title is not None and title.strip():
        updates["title"] = title
    if description is not None:
        updates["description"] = description
        
    if not updates:
        raise ValueError("At least one field (title or description) must be provided")
        
    result = storage.update_todo(todo_id, updates)
    if result is None:
        raise ValueError(f"Todo with ID {todo_id} not found")
    return result

@tool
def delete_todo(todo_id: str) -> bool:
    """Delete a todo item.
    Args:
        todo_id: The unique identifier of the todo to delete
        
    Returns:
        bool: True if the todo was deleted, False if not found
    """
    if not todo_id:
        raise ValueError("Todo ID is required")
    return storage.delete_todo(todo_id)

@tool
def list_todos(status: Optional[str] = None) -> List[Dict]:
    """List all todos, optionally filtered by status.
    Args:
        status: Optional filter for todo status ('pending' or 'completed')
        
    Returns:
        list: List of matching todo items
    """
    if status and status not in ["pending", "completed"]:
        raise ValueError("Status must be either 'pending' or 'completed'")
    return storage.list_todos(status)

@tool
def toggle_todo(todo_id: str) -> Dict:
    """Toggle the completion status of a todo item.    
    Args:
        todo_id: The unique identifier of the todo to toggle
        
    Returns:
        dict: The updated todo item
    """
    if not todo_id:
        raise ValueError("Todo ID is required")
        
    result = storage.toggle_todo(todo_id)
    if result is None:
        raise ValueError(f"Todo with ID {todo_id} not found")
    return result

@tool
def get_todo(todo_id: str) -> Dict:
    """Get a specific todo item by ID.
    Args:
        todo_id: The unique identifier of the todo to retrieve
        
    Returns:
        dict: The requested todo item
    """
    if not todo_id:
        raise ValueError("Todo ID is required")
        
    result = storage.get_todo(todo_id)
    if result is None:
        raise ValueError(f"Todo with ID {todo_id} not found")
    return result 