from pydantic import BaseModel
from typing import List 
class ReceitaBase(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str 

class Receita(ReceitaBase):
    id: int