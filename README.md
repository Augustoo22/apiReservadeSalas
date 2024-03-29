# Controle e Reserva de Salas de Aula API

A API de Controle e Reserva de Salas de Aula é uma aplicação Django desenvolvida para gerenciar o uso de salas de aula em uma instituição educacional. Ela fornece endpoints RESTful para realizar operações CRUD (Create, Read, Update, Delete) em salas de aula, horários e reservas.

## Funcionalidades Principais

- **Listagem de Salas de Aula**: Visualize todas as salas de aula disponíveis.
- **Detalhes da Sala de Aula**: Obtenha informações detalhadas sobre uma sala de aula específica.
- **Criação de Salas de Aula**: Adicione novas salas de aula ao sistema.
- **Atualização de Salas de Aula**: Atualize os detalhes de uma sala de aula existente.
- **Exclusão de Salas de Aula**: Remova salas de aula do sistema.
- **Listagem de Horários Disponíveis**: Veja os horários disponíveis para uma sala de aula específica.
- **Reserva de Salas de Aula**: Reserve uma sala de aula para um horário específico.
- **Cancelamento de Reservas**: Cancelamento de reservas de salas de aula existentes.

## Configuração e Uso

1. **Instalação de Dependências**:
   ```
   pip install -r requirements.txt
   ```

2. **Execução de Migrações**:
   ```
   python manage.py migrate
   ```

3. **Iniciar o Servidor de Desenvolvimento**:
   ```
   python manage.py runserver
   ```

4. **Acesso aos Endpoints**:
   Os endpoints da API podem ser acessados através de um cliente HTTP ou navegador.

## Exemplos de Requisições

- **Listar todas as salas de aula**:
  ```
  GET /api/salas/
  ```

- **Visualizar detalhes de uma sala de aula específica**:
  ```
  GET /api/salas/<id>/
  ```

- **Criar uma nova sala de aula**:
  ```
  POST /api/salas/criar/
  ```

- **Atualizar os detalhes de uma sala de aula existente**:
  ```
  PUT /api/salas/<id>/atualizar/
  ```

- **Excluir uma sala de aula existente**:
  ```
  DELETE /api/salas/<id>/excluir/
  ```

- **Listar horários disponíveis para uma sala de aula específica**:
  ```
  GET /api/salas/<id>/horarios/
  ```

- **Reservar uma sala de aula para um determinado horário**:
  ```
  POST /api/salas/<id>/reservar/
  ```

- **Cancelar uma reserva de sala de aula existente**:
  ```
  DELETE /api/reservas/<id>/cancelar/
  ```

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---
