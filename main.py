from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from typing import List
from schema import ReceitaBase, Receita

app = FastAPI(title= "API da Raira")


receitas: List[Receita] = []

@app.get("/", status_code=HTTPStatus.OK)
def hello():
    return{"title" : "Livro de Receitas"}

@app.get("/receitas",response_model=List[Receita], status_code=HTTPStatus.OK)
def listar_receitas():
    return receitas

@app.get("/receitas/id/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_id(id: int):
    for receita in receitas:
        if receita.id == id:
            return receita
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

@app.get("/receitas/{nome_receita}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_nome(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return receita
    
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")


@app.post("/receitas", response_model=Receita, status_code=HTTPStatus.CREATED)
def create_receita(dados: ReceitaBase):
    for r in receitas:
        if r.nome.lower() == dados.nome.lower(): #verica se já existe uma receita com esse nome
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Já existe uma receita com esse nome!")

    novo_id = 1 if len(receitas) == 0 else receitas[-1].id + 1
    nova_receita = Receita(
        id=novo_id,
        nome=dados.nome,
        ingredientes=dados.ingredientes,
        modo_de_preparo=dados.modo_de_preparo
    )
    receitas.append(nova_receita)
    return nova_receita

@app.put("/receitas/{id}", response_model=Receita,  status_code=HTTPStatus.OK)
def update_receita(id: int, dados: ReceitaBase):
    for r in receitas:
        if r.nome.lower() == dados.nome.lower() and r.id != id: #Verifica se existe uma receita com esse nome
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Já existe uma receita com esse nome!")
    if dados.nome.strip() == "" or dados.modo_de_preparo.strip() == "":
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Nome ou modo de preparo não podem ser vazios!")
    for ingrediente in dados.ingredientes:
        if ingrediente.strip() == "":
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Ingredientes não podem ser vazios!")
        
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo,
            )
            receitas[i] = (receita_atualizada)
            return receita_atualizada
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

@app.delete("/receitas/{id}",response_model=Receita, status_code=HTTPStatus.OK)
def delete_receita(id: int):
    if len(receitas) == 0:
        return {"mensagem": "Não há receitas para deletar."}
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_deletada = receitas.pop(i) 
            return {
                "mensagem": f"A receita '{receita_deletada.nome}' foi deletada com sucesso.",
                "receita": receita_deletada
            }
    
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")
            

   
    