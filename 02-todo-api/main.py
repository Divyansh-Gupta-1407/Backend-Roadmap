from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Todo Application")


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    deadline: Optional[datetime] = None


class Todo(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    created_at: datetime
    completed: bool = False
    completed_at: Optional[datetime] = None
    deadline: Optional[datetime] = None


todos: list[Todo] = []


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