from pydantic import BaseModel  # Cauã Moreira Schmidt

class Produto(BaseModel):   # The attributes that were set None are optional
    id_produto: int = None
    nome: str
    descricao: str
    foto: bytes
    valor_unitario: float