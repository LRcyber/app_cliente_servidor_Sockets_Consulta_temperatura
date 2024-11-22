import socket

# Configuração do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5500         # Porta do servidor

# Criação e conexão do socket do cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    print("Conectado ao servidor.")

    # Solicitação para obter a temperatura
    mensagem_solicitacao = "temperatura\n"  # Solicita a temperatura
    cliente.sendall(mensagem_solicitacao.encode('utf-8'))
    print(f"Solicitação enviada: {mensagem_solicitacao.strip()}")

    # Espera pela resposta do servidor
    resposta = cliente.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {resposta}")
