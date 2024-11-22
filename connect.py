from app.default import Pessoa
from tinydb import TinyDB

bd = TinyDB("Pessoa.json")
def inserir(main: Pessoa):
    bd.insert({"Nome":main.nome,"Telefone":main.telefone,"Email":main.email,"Senha":main.senha,})
    
    def mostrarTodos():
        todos = bd.all()
        return todos
