import sqlite3

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect("tabelaF.db")

# Criar um objeto cursor para executar comandos SQL
c = conn.cursor()

# Criar a tabela de fornecedores
c.execute('''
    CREATE TABLE fornecedor (
    id INT,
    nome VARCHAR(150) NOT NULL,
    endereco VARCHAR(150),
    produtos VARCHAR(20));
''')


c.execute(""""
INSERT INTO fornecedor (id,nome,endereco,produto) VALUES (1,"Empresa de Leite Parmaleite", "Rua dos Leites,23","Leite);
INSERT INTO fornecedor (id,nome,endereco,produto) VALUES (2,"Peixaria Abril", "Rua dos leites,25","Peixe);
INSERT INTO fornecedor (id,nome,endereco,produto) VALUES (3,"Acougue Legal", "Rua dos leites,30","Carnes");
INSERT INTO fornecedor (id,nome,endereco,produto) VALUES (4,"Acougue novo", "Rua dos leites,35","Carnes");
INSERT INTO fornecedor (id,nome,endereco,produto) VALUES (5,"Padaria do Pão", "Rua dos leites,65","Paes");
INSERT INTO fornecedor (id,nome,endereco,produto) VALUES (6,"Marcenaria Martelo", "Rua dos leites,99","Madeiras");
"""
)
c.execute("""
        UPDATE fornecedor SET endereco = 'Rua dos Peixes, 26' WHERE id = 2;
        """)

c.execute(""""
        Select * from fornecedor
""")

c.execute("""
        SELECT * FROM fornecedor WHERE produtos ='carnes';
""")

c.execute("""
        DELETE FROM fornecedor WHERE id=1;
""")

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()