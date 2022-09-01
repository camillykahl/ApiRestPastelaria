from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class Cliente(BaseModel):
    codigo: int = None
    nome: str
    cpf: str
    telefone: str = None
    compra_fiado: int
    dia_fiado: int	
    senha: str = None

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE
@router.get("/cliente/{id}", tags=["cliente"])
def get_cliente(id: int):
	return {"msg": "get executado", "id": id}, 200

@router.post("/cliente/{id}", tags=["cliente"])
def post_cliente(id: int, c: Cliente):
	return {"msg": "post executado", "id": id, "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone}, 200

@router.put("/cliente/{id}", tags=["cliente"])
def put_cliente(id: int, c: Cliente):
	return {"msg": "put executado", "id": id, "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone}, 201

@router.delete("/cliente/{id}", tags=["cliente"])
def delete_cliente(id: int):
	return {"msg": "delete executado", "id": id}, 201