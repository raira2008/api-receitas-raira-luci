from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title= "API da Raira")

class ReceitaBase(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str 

class Receita(ReceitaBase):
    id: int

receitas: List[Receita] = []



@app.get("/receitas/{nome_receita}")
def get_receita_por_nome(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return receita
    
    return{"receita não encontrada"}

@app.get("/receitas/id/{id}")
def get_receita_por_id(id: int):
    for receita in receitas:
        if receita.id == id:
            return receita
        return{"receita não encontrada"}



@app.post("/receitas")
def create_receita(dados: Receita):
    nova_receita = dados
    
    novo_id = 1 if len(receitas) == 0 else receitas[-1].id + 1
    nova_receita = Receita(
        id=novo_id,
        nome=dados.nome,
        ingredientes=dados.ingredientes,
        modo_de_preparo=dados.modo_de_preparo
    )

    
    receitas.append(nova_receita)
   
    return nova_receita