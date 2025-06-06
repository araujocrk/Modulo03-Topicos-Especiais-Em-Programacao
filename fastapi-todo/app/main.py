# 1. Cria e entra no diretorio/pasta
# 2. uv venv no terminal (cria a pasta do ambiente virtual)
# 3. Ativar o ambiente virtual
# 4. uv init --app no terminal (Iniciar projeto)
# 5. uv add fastapi --extra standard no terminal (add fastapi e outras dependências)
# 6. uv run fastapi dev (Rodar projeto)
# Se necessário ctrl + shift + p --> Python: Select Interpreter --> Enter interpreter path --> Path venv/Scripts/python.exe (Erro de importação no vscode)

from fastapi import FastAPI, HTTPException, Query, Path, status
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    
class Task(TaskCreate):
    id: str
    created_at: datetime

app = FastAPI(
    title="API de Tarefas",
    description="API para gestão de tarefas a fazer",
    version="0.1.0"
)

tasks_db = {}

@app.get("/tasks", response_model=List[Task], status_code=status.HTTP_200_OK)
def list_tasks(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0)):
    """
    Lista de tarefas com paginação via query string.
    """
    tasks = list(tasks_db.values())
    return tasks[skip: skip + limit]

@app.get('/tasks/{task_id}', response_model=Task, status_code=status.HTTP_200_OK)
def get_task(task_id: str = Path(...)):
    """
    Busca uma tarefa pelo ID via parâmetro de URL.
    """
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    return task

@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """
    Cria uma nova tarefa via corpo da requisição.
    """
    task_id = str(uuid4())
    new_task = Task(id=task_id, created_at=datetime.timezone.utc(), **task.model_dump()) **task.list() # **task.list() datetime.utcnow() are deprecated
    tasks_db[task_id] = new_task
    return new_task

@app.post('/tasks/{task_id}', response_model=Task, status_code=status.HTTP_200_OK)
def update_task(task_id: str, task: TaskCreate):
    """
    Atualiza uma tarefa existente.
    """
    stored_task = tasks_db.get(task_id)
    if not stored_task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    updated_task = Task(id=task_id, created_at=stored_task.created_at, **task.model_dump()) # **task.list()  is deprecated
    tasks_db[task_id] = updated_task
    return updated_task

@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    """
    Remove uma tarefa.
    """
    if task_id in tasks_db:
        del tasks_db[task_id]
    else:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')