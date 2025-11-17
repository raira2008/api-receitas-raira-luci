from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import User, table_registry

app = FastAPI(title = 'API de teste')

#Cria engine (Aqui com SQlite em memória)
engine = create_engine("sqlite:///:memory:", echo=False)

#Cria as tabelas
table_registry.metadata.create_all(engine)

#Cria uma sessão
with Session(engine) as session:
    aluno = User(
        nome_usuario = "rairaalves", senha = "senha123", email = "raira@email.com"
    )
    session.add(aluno)
    session.commit()
    session.refresh(aluno)

print("DADOS DO USUÁRIO:", aluno)
print("ID:", aluno.id)
print("Criado em:", aluno.created_at)
