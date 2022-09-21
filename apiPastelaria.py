from fastapi import FastAPI
import db
from mod_funcionario.FuncionarioModel import FuncionarioDB
from mod_funcionario import FuncionarioDAO
from mod_cliente.ClienteModel import ClienteDB
from mod_cliente import ClienteDAO
from mod_produto.ProdutoModel import ProdutoDB
from mod_produto import ProdutoDAO
#import mod_produto.ProdutoDAO as ProdutoDAO

app = FastAPI()

app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

db.criaTabelas()