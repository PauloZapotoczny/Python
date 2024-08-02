import pyodbc
from datetime import date

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-JRR030Q\SQLEXPRESS;"
    "Database=PythonIntegration;"
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

id = 5
cliente = "Eduardo"
produto = "Chaveiro"
data = date.today()
preco = 20
quantidade = 4

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()
