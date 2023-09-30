# GenRoomAPP
O GenRoomAPP é um aplicativo desenvolvido em Python usando o framework Kivy. Ele foi criado com o propósito de facilitar a gestão e reserva de salas e recursos compartilhados na Faculdade Santa-Terezinha-CEST, através da integração com a API GenRoom, para proporcionar uma experiência de usuário eficiente e intuitiva.

# Visão Geral
O principal objetivo do GenRoomAPP é otimizar e simplificar o processo de reserva de salas, recursos e espaços compartilhados na Faculdade Santa-Terezinha-CEST. Com este aplicativo, os usuários têm a capacidade de:
* - Criar Salas: Permite aos usuários criar novas salas, inserindo detalhes como capacidade, tipo, e descrição.
* - Listar Salas: Oferece uma visão global de todas as salas disponíveis, fornecendo informações detalhadas sobre cada uma delas.
* - Reservar uma Sala: Os usuários podem fazer reservas com base nas necessidades e disponibilidades, simplificando o agendamento de aulas e eventos.
* - Visualizar Salas Ocupadas: Mostra uma visão em tempo real das ocupações das salas, facilitando o planejamento.
* - Reservar Salas por Período: Permite a reserva de salas em intervalos específicos, otimizando o uso dos espaços disponíveis.
* - Reservar Recursos Compartilhados: Além de salas, o aplicativo também permite a reserva de recursos como laboratórios, projetores e outros equipamentos.

# Estrutura do Projeto
O projeto GenroomAPP segue a seguinte estrutura de diretórios:

# Pré-requisitos
* Python 3.x
* Kivy
* Dependências listadas em requirements.txt

# Como Executar
* - Clone este repositório para o seu sistema local.
* - Crie e ative um ambiente virtual (recomendado).
* - Instale as dependências usando pip install -r requirements.txt.
* - Execute o aplicativo com python main.py.

# Conexão com a API
O aplicativo GenRoomAPP está em fase avançada de desenvolvimento, implementando a integração com a API GenRoom, promovendo uma sincronização de dados ágil e em tempo real com o banco de dados da Faculdade Santa-Terezinha-CEST. Esta integração está sendo desenvolvida para possibilitar uma série de operações, tais como:

* Criação de Salas: O aplicativo permite a criação de novas salas diretamente, com os dados sendo imediatamente refletidos no banco de dados central através da API.

* Atualização de Salas: Os usuários podem atualizar detalhes específicos das salas, como nome, capacidade e descrição, e tais alterações são prontamente refletidas no banco de dados.

* Consulta de Salas: O aplicativo busca dados em tempo real do banco de dados, permitindo aos usuários visualizar detalhes atualizados das salas.

A arquitetura modular e robusta da nossa aplicação e API permite uma expansão futura fácil e eficiente, abrindo caminho para a adição de novas funcionalidades e melhorias.

## Como Funciona a Conexão com a API
O aplicativo se conecta à API GenRoom utilizando o protocolo HTTP, mais especificamente através de requisições GET para buscar dados e POST e PUT para criar e atualizar dados, respectivamente.

´url = 'http://127.0.0.1:5001/api/rooms'
response = requests.get(url)

if response.status_code == 200:
    rooms = response.json()
    # Processar os dados recebidos
else:
    print(f'Error fetching rooms: {response.status_code}')´