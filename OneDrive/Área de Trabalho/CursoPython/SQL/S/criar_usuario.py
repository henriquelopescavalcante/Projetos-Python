import sqlite3
import hashlib

conexao = sqlite3.connect("redes.sqlite3")
cursor = conexao.cursor()

nome = input("Digite seu nome:")
email = input("Digite seu email:")
while true:
    senha = input("Digite sua senha:")
    confirma_senha = input("Confirme sua senha:")
    if senha == confirma_senha:
        break
    else:
        print("A confirmacao de senha esta errada!")

sql = "insert into usuario (nome, email, senha) values (?,?,?)"

senha = hashlib.sha256(senha.encode("utf-8")).hexdigest()
valores = [nome, email, senha]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()
