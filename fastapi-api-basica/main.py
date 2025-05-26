# Terminal 
# pip install fastapi[all]
# pip install pydantic

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import HTTPException

# Inicializando o app FastAPI
app = FastAPI()

# Modelo de dados da tarefa
class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str | None = None  # Campo opcional
    concluida: bool = False
    
tarefas = []

@app.post('/tarefas')
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return {
                'status_code': status.HTTP_201_CREATED,
                'content': {'mensagem': 'Tarefa criada com sucesso!', 'tarefa': tarefa.model_dump()}
            }
    
@app.get('/tarefas/{id}')
def buscar_tarefa(id: int):
    if id < 0 or id >= len(tarefas):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tarefa não encontrada'
        )
    return tarefas[id]