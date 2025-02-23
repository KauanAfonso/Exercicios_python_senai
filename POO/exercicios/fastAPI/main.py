'''
Crie um sistema de gerenciamento de tarefas onde você tem tarefas com prioridades, 
datas de vencimento, status (pendente, em andamento, concluída) e categorias. 
Implemente funcionalidades de criar, editar, listar e excluir tarefas, além de filtros por 
status e prioridade. 

'''


from fastapi import FastAPI

app = FastAPI()

lista_tarefas = [
    {"id": 1, "nome": "Lavar o carro" , "data_vencimento" : "20/12/2025", "status": "Pendente", "categoria": "prioridades"},
    {"id": 2, "nome": "Fazer jantar" , "data_vencimento" : "20/12/2025", "status": "Pendente", "categoria": "prioridades"},
    {"id": 3, "nome": "Fazer jantar" , "data_vencimento" : "20/12/2025", "status": "Pendente", "categoria": "prioridades"},
]

@app.get("/tarefas")
def ler_tarefas():
    return lista_tarefas

@app.get("/tarefas/{id}")
def ler_tarefa_especifica(id: int):
    for tarefa in lista_tarefas:
        if tarefa['id'] == id:
            return tarefa
    else:
        return "NÃO ENCONTRADA"
    
@app.post("/criar_tarefa")
def criar_tarefa(id: int, nome: str, data_vencimento: str, status: str, categoria: str):
     tarefa = {"id": id, "nome": nome , "data_vencimento" : data_vencimento, "status": status, "categoria": categoria},
     lista_tarefas.append(tarefa)
     return "Criado com sucesso!"
 
@app.put("./excluir_tarefa")
def excluir_tarefa(id: int):
    for tarefa in lista_tarefas:
        if tarefa.id == id:
            tarefa.remove()    