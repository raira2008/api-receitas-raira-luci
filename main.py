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

@app.get("/")
def hello():
    return{"title" : "Livro de Receitas"}


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

@app.get("/receitas/id/{id}")
def get_receita_por_id(id: int):
    for receita in receitas:
        if receita.id == id:
            return receita
    return{"receita não encontrada"}

@app.post("/receitas")
def create_receita(dados: ReceitaBase):
    for r in receitas:
        if r.nome.lower() == dados.nome.lower():
            return ("Já existe uma receita com esse nome")

    novo_id = 1 if len(receitas) == 0 else receitas[-1].id + 1
    nova_receita = Receita(
        id=novo_id,
        nome=dados.nome,
        ingredientes=dados.ingredientes,
        modo_de_preparo=dados.modo_de_preparo
    )
    receitas.append(nova_receita)
    return nova_receita

@app.put("/receitas/{id}")
def update_receita(id: int, dados: create_receita):
    if not dados.nome.strip() or not dados.modo_de_preparo.strip() or not dados.ingredientes:
        return {"erro": "Nenhum campo pode estar vazio"}
    
    for r in receitas:
        if r.id != id and r.nome.lower() == dados.nome.lower():
            return {"erro": "Já existe uma receita com esse nome"}
    
    for i in range(len(receitas)):
        if receitas [i].id == id:
            receita_atualizada = Receita(
                id = id,
                nome = dados.nome,
                ingredientes = dados.ingredientes,
                modo_de_preparo = dados.modo_de_preparo,
            )
            
            receitas[i] = (receita_atualizada)
            return receita_atualizada
    

    return{"mensagem" : "Receita não encontrada"}


   
    