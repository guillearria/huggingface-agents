import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

class TodoStorage:
    def __init__(self, storage_path: str = "todo_data.json"):
        """Initialize the TodoStorage with a path to the JSON storage file.
        
        Args:
            storage_path (str): Path to the JSON storage file
        """
        self.storage_path = Path(storage_path)
        self._ensure_storage_exists()
        
    def _ensure_storage_exists(self) -> None:
        """Create storage file if it doesn't exist."""
        if not self.storage_path.exists():
            self.storage_path.write_text(json.dumps({"todos": []}))
            
    def _read_storage(self) -> dict:
        """Read the current storage content."""
        try:
            return json.loads(self.storage_path.read_text())
        except json.JSONDecodeError:
            return {"todos": []}
            
    def _write_storage(self, data: dict) -> None:
        """Write data to storage."""
        self.storage_path.write_text(json.dumps(data, indent=2))
        
    def _create_todo_object(self, title: str, description: str = "") -> dict:
        """Create a new todo object with default values."""
        now = datetime.now().isoformat()
        return {
            "id": str(uuid.uuid4()),
            "title": title,
            "description": description,
            "status": "pending",
            "created_at": now,
            "updated_at": now
        }
        
    def add_todo(self, title: str, description: str = "") -> dict:
        """Add a new todo item.
        
        Args:
            title (str): Todo title
            description (str, optional): Todo description
            
        Returns:
            dict: The created todo item
        """
        data = self._read_storage()
        new_todo = self._create_todo_object(title, description)
        data["todos"].append(new_todo)
        self._write_storage(data)
        return new_todo
        
    def get_todo(self, todo_id: str) -> Optional[dict]:
        """Get a specific todo by ID.
        
        Args:
            todo_id (str): The ID of the todo to retrieve
            
        Returns:
            Optional[dict]: The todo item if found, None otherwise
        """
        data = self._read_storage()
        for todo in data["todos"]:
            if todo["id"] == todo_id:
                return todo
        return None
        
    def list_todos(self, status: Optional[str] = None) -> List[dict]:
        """List all todos, optionally filtered by status.
        
        Args:
            status (str, optional): Filter todos by status ('pending' or 'completed')
            
        Returns:
            List[dict]: List of matching todos
        """
        data = self._read_storage()
        if status is None:
            return data["todos"]
        return [todo for todo in data["todos"] if todo["status"] == status]
        
    def update_todo(self, todo_id: str, updates: Dict[str, str]) -> Optional[dict]:
        """Update a todo item.
        
        Args:
            todo_id (str): The ID of the todo to update
            updates (Dict[str, str]): Dictionary of fields to update
            
        Returns:
            Optional[dict]: The updated todo if found, None otherwise
        """
        data = self._read_storage()
        for todo in data["todos"]:
            if todo["id"] == todo_id:
                todo.update(updates)
                todo["updated_at"] = datetime.now().isoformat()
                self._write_storage(data)
                return todo
        return None
        
    def delete_todo(self, todo_id: str) -> bool:
        """Delete a todo item.
        
        Args:
            todo_id (str): The ID of the todo to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        data = self._read_storage()
        initial_length = len(data["todos"])
        data["todos"] = [todo for todo in data["todos"] if todo["id"] != todo_id]
        if len(data["todos"]) < initial_length:
            self._write_storage(data)
            return True
        return False
        
    def toggle_todo(self, todo_id: str) -> Optional[dict]:
        """Toggle the status of a todo between 'pending' and 'completed'.
        
        Args:
            todo_id (str): The ID of the todo to toggle
            
        Returns:
            Optional[dict]: The updated todo if found, None otherwise
        """
        todo = self.get_todo(todo_id)
        if todo:
            new_status = "completed" if todo["status"] == "pending" else "pending"
            return self.update_todo(todo_id, {"status": new_status})
        return None 