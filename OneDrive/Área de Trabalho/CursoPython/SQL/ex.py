import sqlite3

conexao = sqlite3.connect("db.sqlite3")
cursor = conexao.cursor()
sql = """
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL UNIQUE
    data TEXT
    local TEXT
);
''')

# Criar a tabela de organizador
c.execute('''
CREATE TABLE IF NOT EXISTS organizador (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT, NOT NULL
    cpf TEXT 
    id_eventos INTEGER,
    FOREIGN KEY (id_eventos) REFERENCES eventos(id)
);
''')

"""
(sql)
conexao.commit()
conexao.close()