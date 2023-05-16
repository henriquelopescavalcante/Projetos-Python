import socket

HOST = " 201.92.162.212"
PORT = 9000
print("iniciando o socket")
s = socket.socket()
s.bind((HOST, PORT))
s.listen()
conexao, endereco = s.accept()
with conexao:
    print("nova conexao {endereco}")
    while True:
        dados = conexao.recv(1024)
        if not dados:
            break
        texto = dados.decode("utf-8")
        numero1, numero2 = texto.split("x")
        nuemro1 = int(numero1)
        numero2 = int(numero2)
        resultado = numero1 + numero2
        resultado = str(resultado)
        print(f"servidor recebi {texto}")
        conexao.sendall(texto.encode{"utf-8"})

s.close()