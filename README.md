# **Avaliação Técnica**
* Organização e clareza do código
* Estruturação da arquitetura e desacoplamento
* Boas práticas de API com FastAPI
* Modelagem e persistência em MongoDB
* Implementação de integração externa
* Qualidade geral da solução, documentação e organização do projeto

---

# **Descrição do Desafio**

Você deverá desenvolver uma **API para gerenciamento de Leads** utilizando **Python, FastAPI e MongoDB**, seguindo os requisitos descritos abaixo.

---

# **1. Funcionalidades da API**

### **POST /leads**

Cria um lead contendo os campos enviados pelo usuário:

```
name   (string)
email  (string)
phone  (string)
```

Durante o cadastro, o sistema deverá **consultar um serviço externo** (item 2) para preencher automaticamente o campo birth_date e então persistir o lead no MongoDB.

### **GET /leads**

Lista todos os leads cadastrados.

### **GET /leads/{id}**

Retorna os detalhes de um lead específico pelo seu ID.

---

# **2. Integração Externa (Obrigatória)**

Durante a criação de um lead (POST), você deverá consumir a API pública:

```
https://dummyjson.com/users/1
```

Da resposta, extraia o campo:

```
birthDate
```

Esse valor deve ser armazenado no documento do lead como:

```
birth_date
```

### **Regras da Integração Externa:**
1. Em caso de falha na requisição externa, você pode:

   * retornar erro amigável **ou**
   * definir `birth_date = null`

   A decisão é sua, mas deve estar documentada no README.

2. O retorno do lead criado deve seguir o formato:

```
{
  "id": "...",
  "name": "...",
  "email": "...",
  "phone": "...",
  "birth_date": "1998-02-05"
}
```

# **3. Arquitetura Esperada**

Não exigimos uma arquitetura específica, porém será bem avaliado se houver:

* Separação clara entre camadas
* Código limpo e organizado
* Baixo acoplamento e responsabilidades bem definidas
* Estrutura de pastas simples, clara e escalável
* Docker configurado

---

# **4. Entrega**

O repositório deve conter:

* Código fonte organizado
* Arquivo **README.md** com:

  * Instruções claras para rodar o projeto
  * Como iniciar o MongoDB (local ou Docker)
  * Como testar manualmente os endpoints
  * Explicação rápida da arquitetura adotada
  * Comportamento esperado em caso de falha da API externa
