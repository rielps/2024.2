# Docker compose com Django e banco de dados

## Informações gerais

- Assunto: Docker, conteinizar aplicações web
- Disciplina: *sistemas operacionais*

## Relatório

### Aluno

- nome: Jesrriel Moura Lopes
- matrícula: 20232014040016

### Relato
Para a realização da atividade foi criada uma branch chamada docker no repositório do PDS web Bizzu e nela foram criados dois arquivos: Dockerfile e docker-compose.yml. <br>

Inicialmente, no arquivo Dockerfile foi implementado um código que tinha como objetivo criar a imagem da aplicação com base na imagem python sendo instalada dentro desse container /bizzu que foi criado nesse mesmo arquivo. Além da imagem, foram instaladas todas as dependências que estão especificadas no arquivo requirements.txt. 
Mas, com isso, apenas criamos a imagem, não fazendo a execução em nenhum momento, e por isso criamos o arquivo docker-compose.yml para conseguirmos fazer a execução com a criação de um service. Dentro desse service, configuramos algumas coisas para que a aplicação pudesse funcionar, como:<br>

- Build: Palavra-chave que indica o path que ele precisa fazer para chegar até o dockerfile, que é o que ele precisa construir. Usamos o . pois eles estão no mesmo diretório.

- Command: Comando que ele precisa executar para rodar a aplicação. Usamos o bash -c para concatenar os dois comandos, o de migrate e o de runserver, pois normalmente para rodar uma aplicação Django é necessário executar esses dois comandos.

- Ports: Em que porta a aplicação está e a porta do container para conectar os dois.<br><br>
Para a representação do banco de dados foi necessária a alteração do arquivo de settings para que, em vez do SQLite, ele usasse o POSTGRES. Mas, para isso, primeiro adicionamos um novo service no docker-compose e configuramos algumas coisas para tal:<br>

- container_name: Nomear o container que vai armazenar o banco.
- ports: Conectar a porta do container à porta do banco.
- image: Para consumir a imagem do postgres.
- environment: Adicionar informações de conexão, como user e senha, que são variáveis de ambiente.
- Volumes: Local de armazenamento persistente de informações.<br>
Com isso, criamos um novo service chamado DB, que coloca nosso banco postgres em um container. <br>
Não foi necessária a criação de um novo arquivo Dockerfile, pois o postgres já tem sua própria imagem que será usada da forma que foi fornecida, sem adição de novos recursos. <br>

### Arquivos docker e de configuração do django
Como os arquivos não são suportados em markdown, colocarei no mesmo diretório que está o relatório. O nome já exemplifica o que contém em cada arquivo: o Dockerfile é o Dockerfile e o settings são as configurações do nosso projeto no Django.
