import http.client
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def fazer_requisicao():
    conexao = http.client.HTTPConnection("localhost", 8000)
    conexao.request("GET", "/")
    resposta = conexao.getresponse()
    conteudo = resposta.read().decode("utf-8")
    print(f"Status: {resposta.status} | Motivo: {resposta.reason}")
    conexao.close()

def executar_clientes_simultaneos(num_clientes):
    tempo_inicio = time.time()
    with ThreadPoolExecutor(max_workers=num_clientes) as executor:
        executor.map(lambda _: fazer_requisicao(), range(num_clientes))
    duracao = time.time() - tempo_inicio
    print(f"\nCompletou {num_clientes} requisições em {duracao:.4f} segundos")

if __name__ == "__main__":
    clientes = int(input("Digite o número de clientes simultâneos: "))
    executar_clientes_simultaneos(clientes)