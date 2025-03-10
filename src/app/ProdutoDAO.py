from fastapi import APIRouter
from domain.entities.Produto import Produto

router = APIRouter()

# Creating the routes/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"])  # List all
async def get_produto():
    return {"msg": "get todos executado"}, 200

@router.get("/produto/{id}", tags=["Produto"])  # List one
async def get_produto(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/produto/", tags=["Produto"]) # Inserts a new 
async def post_produto(corpo: Produto):
    return {"msg": "post executado",
            "nome": corpo.nome,
            "descrição": corpo.descricao,
            "foto": corpo.foto,
            "valor unitário": corpo.valor_unitario}, 200

@router.put("/produto/{id}", tags=["Produto"])  # Edits one
async def put_produto(id: int, corpo: Produto):
    return {'msg': "put executado",
            "id": id,
            "nome": corpo.nome,
            "descrição": corpo.descricao,
            "foto": corpo.foto,
            "valor unitário": corpo.valor_unitario}, 200

@router.delete("/produto/{id}", tags=["Produto"])   # Deletes one
async def delete_produto():
    return {"msg": "delete executado"}, 200