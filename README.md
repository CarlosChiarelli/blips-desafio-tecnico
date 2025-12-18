# Leads API

API para gerenciamento de leads construída com **FastAPI** e **MongoDB**, seguindo os requisitos do arquivo `README_TEST.md`.

## Como executar

- **Requisitos**: Docker e Docker Compose.
- Ajuste o arquivo `.env.example` se quiser alterar portas ou credenciais (o `docker-compose` já carrega esse arquivo).
- Suba os containers:

```bash
cd docker
docker compose up --build
```

- A aplicação ficará disponível em `http://localhost:8000` (ajuste a porta com `APP_PORT` se necessário).
- Documentação interativa (Swagger UI): `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

### Serviços do Compose

- `blips-app`: API FastAPI.
- `mongodb`: Banco MongoDB com usuário `root`/`example`.
- `mongo-express`: UI opcional em `http://localhost:8081` para navegar no MongoDB.

## Testes manuais dos endpoints

Passo a passo usando a UI do Swagger e cURL para conferir o funcionamento ponta a ponta:

1. Abra a documentação interativa: `http://localhost:8000/docs`.

2. No endpoint `POST /leads`, crie dois leads (exemplos):
   - Lead 1:
   ```json
   {
     "name": "Ada Lovelace",
     "email": "ada@example.com",
     "phone": "+55 11 99999-9999"
   }
   ```
   - Lead 2:
   ```json
   {
     "name": "Alan Turing",
     "email": "alan@example.com",
     "phone": "+44 20 1234-5678"
   }
   ```

   A API buscará `birth_date` na DummyJSON; se houver falha, salva `null`.

3. Liste todos os leads em `GET /leads` (via Swagger ou cURL):
   ```bash
   curl http://localhost:8000/leads
   ```

4. Pegue o campo `id` de um dos itens retornados e consulte-o em `GET /leads/{id}`:
   ```bash
   curl http://localhost:8000/leads/<id>
   ```

5. Abra o Mongo Express em `http://localhost:8081`, acesse o database `blips` (ou o nome configurado em `MONGODB_DB`), navegue até a coleção `leads` e confirme que os registros criados aparecem lá com os mesmos dados.

## Comportamento da integração externa

- Endpoint consumido: `https://dummyjson.com/users/1`.
- Campo extraído: `birthDate`, armazenado como `birth_date`.
- Qualquer erro ou resposta inválida da API externa resulta em `birth_date = null` no lead criado (decisão documentada conforme requisito).

## Arquitetura adotada

- `src/main.py`: criação do app FastAPI e ciclo de vida (Mongo + cliente HTTP).
- `src/api/`: roteadores HTTP; `leads` expõe `POST /leads`, `GET /leads`, `GET /leads/{id}`.
- `src/schemas/`: contratos Pydantic de entrada/saída.
- `src/clients/`: integração externa (DummyJSON).
- `src/repositories/`: persistência MongoDB (Motor).
- `src/services/`: regras de negócio e orquestração entre camadas.
- `src/core/config.py`: carregamento de configuração via variáveis de ambiente.

## Variáveis de ambiente

- `APP_PORT`: porta exposta pela aplicação (default `8000`).
- `MONGODB_URI`: string de conexão do MongoDB (default aponta para o serviço `mongodb` do Compose).
- `MONGODB_DB`: nome do database utilizado (default `blips`).
- `DUMMY_USER_URL`: endpoint da API externa (default `https://dummyjson.com/users/1`).

## Rodando sem Docker (opcional)

```bash
poetry install
poetry run uvicorn src.main:app --reload --port 8000
```

Certifique-se de ter um MongoDB acessível e ajuste `MONGODB_URI`/`MONGODB_DB` conforme necessário.

É possível executar a API simplesmente com um comando `make api`.

Para levantar o ambiente de desenvolvimento basta ter um ambiente `linux` e utilizar a `IDE vscode` com a extensão `devcontainer`, então "buildar" o devcontainer na raiz do projeto.
