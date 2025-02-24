from fastapi import APIRouter
from domain.entities.Cliente import Cliente

router = APIRouter()

# Creating the routes/endpoints: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])  # List all
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])  # List one
def get_cliente(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/cliente/", tags=["Cliente"]) # Inserts a new 
def post_cliente(corpo: Cliente):
    return {"msg": "post executado",
            "nome": corpo.nome,
            "cpf": corpo.cpf,
            "telefone": corpo.telefone}, 200

@router.put("/cliente/{id}", tags=["Cliente"])  # Edits one
def put_cliente(id: int, corpo: Cliente):
    return {'msg': "put executado",
            "id": id,
            "nome": corpo.nome,
            "cpf": corpo.cpf,
            "telefone": corpo.telefone}, 200

@router.delete("/cliente/{id}", tags=["Cliente"])   # Deletes one
def delete_cliente():
    return {"msg": "delete executado"}, 200