from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from typing import List
from schema import ReceitaBase, Receita, Usuario, BaseUsuario, UsuarioPublic

app = FastAPI(title= "API da Raira")

usuarios: List[Usuario] = []
receitas: List[Receita] = []

@app.get("/", status_code=HTTPStatus.OK)
def hello():
    return{"title" : "Livro de Receitas"}

@app.get("/receitas",response_model=List[UsuarioPublic], status_code=HTTPStatus.OK)
def listar_usuarios():
    return usuarios

@app.get("/usuarios",response_model=List[UsuarioPublic], status_code=HTTPStatus.OK)
def listar_receitas():
    return receitas

@app.get("/receitas/id/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_id(id: int):
    for receita in receitas:
        if receita.id == id:
            return receita
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

@app.get("/usuarios/id/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_id(id: int):
    for usuario in usuarios:
        if usuario.id == id:
            return usuario
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")

@app.get("/receitas/{nome_receita}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_nome(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return receita
    
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

@app.get("/usuarios/{nome_usuario}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_nome(nome_usuario: str):
    for usuario in usuarios:
        if usuario.nome_usuario == nome_usuario:
            return usuario
    
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")


@app.post("/receitas", response_model=Receita, status_code=HTTPStatus.CREATED)
def create_receita(dados: ReceitaBase):
    for r in receitas:
        if r.nome.lower() == dados.nome.lower(): #verica se já existe uma receita com esse nome
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Já existe uma receita com esse nome!")
    if dados.nome.strip() == "" or dados.modo_de_preparo.strip() == "":
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Nome ou modo de preparo não podem ser vazios!")
    for ingrediente in dados.ingredientes:
        if ingrediente.strip() == "":
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Ingredientes não podem ser vazios!")
    novo_id = 1 if len(receitas) == 0 else receitas[-1].id + 1
    nova_receita = Receita(
        id=novo_id,
        nome=dados.nome,
        ingredientes=dados.ingredientes,
        modo_de_preparo=dados.modo_de_preparo
    )
    receitas.append(nova_receita)
    return nova_receita

@app.post("/usuarios", status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_usuario(dados: BaseUsuario):
    for u in usuarios:
        if u.email.lower() == dados.email.lower().strip(): 
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Já existe um usuário cadastrado com esse e-mail!")
    if dados.nome_usuario.strip() == "" or dados.email.strip() == "":
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Nome do usuário ou email não podem ser vazios!")
    for senha in dados.senha:
        if senha.strip() == "":
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Senha não pode ser vazio!")
    novo_id = 1 if len(usuarios) == 0 else usuarios[-1].id + 1
    novo_usuario = Usuario(
        id=novo_id,
        nome_usuario=dados.nome_usuario,
        senha=dados.senha,
        email=dados.email
    )
    usuarios.append(novo_usuario)
    return UsuarioPublic(
        id= novo_usuario.id,
        nome_usuario= novo_usuario.nome_usuario,
        email= novo_usuario.email
    )

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

@app.put("/usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def update_usuario(id: int, dados: BaseUsuario):
    for u in usuarios:
        if u.email.lower() == dados.email.lower() and u.id != id: #Verifica se existe uma receita com esse nome
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Já existe um usuário com esse nome!")
    if dados.nome_usuario.strip() == "" or dados.email.strip() == "":
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Nome do usuário ou email não podem ser vazios!")
    if dados.senha.strip() == "":
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Senha não pode ser vazio!")
    
    for i in range(len(usuarios)):
        if usuarios[i].id == id:
            usuario_atualizado = Usuario(
                id=id,
                nome_usuario= dados.nome_usuario,
                senha=dados.senha,
                email=dados.email,
            )
            usuarios[i] = usuario_atualizado
            return usuario_atualizado
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")
        

@app.delete("/receitas/{id}",response_model=Receita, status_code=HTTPStatus.OK)
def delete_receita(id: int):
    if len(receitas) == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Não existem receitas para deletar!")
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_deletada = receitas.pop(i) 
            return {
                "mensagem": f"A receita '{receita_deletada.nome}' foi deletada com sucesso.",
                "receita": receita_deletada
            }
    
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

@app.delete("/usuarios/{id}", response_model=dict, status_code=HTTPStatus.OK)
def delete_usuario(id: int):
    if len(usuarios) == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Não existem usuarios para deletar!")
    for i in range(len(usuarios)):
        if usuarios[i].id == id:
            usuario_deletado = usuarios.pop(i) 
            return {
                "mensagem": f"O usuário '{usuario_deletado.nome_usuario}' foi deletado com sucesso.",
                "usuario": usuario_deletado
            }
    
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")


            

   
    