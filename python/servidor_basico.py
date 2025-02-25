import http.server

CONTEUDO_HTML = """
<!DOCTYPE html>
<html>
<head><title>Servidor HTTP Básico</title></head>
<body>
    <h1>Hello world!!!</h1>
    <p>Servidor HTTP Python Básico</p>
</body>
</html>
"""

class GerenciadorRequisicao(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Requisição de: {self.client_address} | Caminho: {self.path}")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(CONTEUDO_HTML.encode("utf-8"))

if __name__ == "__main__":
    servidor = http.server.HTTPServer(("", 8000), GerenciadorRequisicao)
    print("Servidor rodando na porta 8000...")
    servidor.serve_forever()