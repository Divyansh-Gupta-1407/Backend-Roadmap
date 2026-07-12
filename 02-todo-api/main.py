from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Todo Application")


# base models 
''' 
TodoCreate: BaseModel to create a todo request
TodoUpdate: BaseModel to update a todo
Todo: BaseModel to created Todo
'''
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    deadline: Optional[datetime] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    completed: Optional[bool] = None

class Todo(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    created_at: datetime
    completed: bool = False
    completed_at: Optional[datetime] = None
    deadline: Optional[datetime] = None
    updated_at: Optional[datetime] = None


# Todo list
todos: list[Todo] = []


# Create a todo route
@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    new_todo = Todo(
        id=uuid4(),
        title=todo.title,
        description=todo.description,
        created_at=datetime.now(),
        completed=False,
        completed_at=None,
        deadline=todo.deadline,
    )

    todos.append(new_todo)

    return new_todo

@app.get("/todos", response_model=list[Todo], status_code=200)
def get_all_todos():
    return todos

@app.get("/todos/{id_target}", response_model=Todo)
def get_by_id(id_target: UUID):
    for todo in todos:
        if todo.id == id_target:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{id_target}", status_code=204)
def delete_todo(id_target: UUID):

    for index, todo in enumerate(todos):

        if todo.id == id_target:
            todos.pop(index)

            return {
                "message": "Todo deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Todo not found")

@app.patch("/todos/{id_target}", response_model=Todo)
def patch_todo(id_target: UUID, todo_update: TodoUpdate):

    for todo in todos:

        if todo.id == id_target:

            update_data = todo_update.model_dump(exclude_unset=True)

            if "title" in update_data:
                todo.title = update_data["title"]

            if "description" in update_data:
                todo.description = update_data["description"]

            if "deadline" in update_data:
                todo.deadline = update_data["deadline"]

            if "completed" in update_data:
                todo.completed = update_data["completed"]

                if todo.completed:
                    todo.completed_at = datetime.now()
                else:
                    todo.completed_at = None

            todo.updated_at = datetime.now()

            return todo

    raise HTTPException(status_code=404, detail="Todo not found")