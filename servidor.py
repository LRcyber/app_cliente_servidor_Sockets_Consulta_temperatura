import socket

# Função para obter a temperatura
def obter_temperatura():
    return "25 GRAUS"  # Simulação de temperatura

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5500         # Porta do servidor

# inicialização e configuração do socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()
    print("Servidor aguardando conexões...")
    
    # conexão do cliente
    conexao, endereco = servidor.accept()
    with conexao:
        print(f"Conexão estabelecida com {endereco}")
        buffer = ""  # Buffer para armazenar dados incompletos

        # Loop para receber dados do cliente
        while True:
            dados = conexao.recv(1024).decode('utf-8')  # Recebe dados do cliente
            if not dados:  # Final da conexão
                print("Conexão encerrada pelo cliente.")
                break
            
            # Adiciona os dados recebidos ao buffer
            buffer += dados

            # Processa as mensagens completas usando o delimitador
            while '\n' in buffer:
                # Separa a mensagem do restante do buffer
                mensagem, buffer = buffer.split('\n', 1)  # Divide a mensagem da próxima parte do buffer
                mensagem = mensagem.strip()  # Remove espaços em branco extras

                print(f"Mensagem recebida do cliente: {mensagem}")

                # Verifica se a mensagem do cliente é para solicitar a temperatura
                if mensagem.lower() == 'temperatura':
                    temperatura = obter_temperatura()
                    # Envia a temperatura de volta ao cliente
                    conexao.sendall(f"A temperatura atual: {temperatura}\n".encode('utf-8'))
                else:
                    conexao.sendall("Comando não reconhecido.\n".encode('utf-8'))
