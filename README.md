# 📦 BuscaCEP - Seu endereço sem stress

Projeto simples e funcional em **Python** que busca informações de um CEP brasileiro usando **Programação Orientada a Objeto (POO)** e consumo de API externa (ViaCEP).

---

## 🚀 Funcionalidades

- 🔢 Entrada de CEP pelo terminal
- ✅ Validação de formato (8 dígitos numéricos)
- 🌐 Consulta automática à API ViaCEP
- 📋 Exibição dos dados de endereço:
  - Logradouro
  - Bairro
  - Cidade
  - Estado
- ⚠️ Tratamento de erros: CEP inválido, conexão falhou, etc.
- 👨‍💻 Código orientado a objetos (POO)

---

## 🛠️ Tecnologias usadas

- [Python 3.10+](https://www.python.org/)
- `requests` para requisições HTTP
- POO: classes, encapsulamento, métodos
- (Opcional) `argparse` ou `typer` para CLI
- (Opcional) `unittest` ou `pytest` para testes

---

## 📂 Estrutura do Projeto

```bash
buscacep/
│
├── main.py # Arquivo principal (entrypoint)
├── cep.py # Classe principal para CEP
├── api_client.py # Lida com requisições à API
├── validador.py # Valida CEPs digitados
├── endereco.py # Classe que representa os dados do endereço
├── utils.py # Funções auxiliares (opcional)
├── tests/ # Testes automatizados (opcional)
│    └── test_cep.py
└── README.md # Este arquivo
```

---

## 💡 Como usar
1 . Clone o repositório
```bash
git clone 
cd city_code_finder
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

> Se não tiver um `requirements.txt`, pode instalar manualmente:

```bash
pip install request
```

3. Rode o programa
```bash
python main.py
```

E digite o CEP quando solicitado.

---

## 🧪 Exemplo de uso

```bash
$ python main.py
Digite o CEP: 01001000

🔍 Buscando...
📍 Rua: Praça da Sé
🏙️ Bairro: Sé
🌆 Cidade: São Paulo
🌎 Estado: SP
✅ Consulta finalizada com sucesso!

```

---

## 🤓 Conceitos aplicados
- Programação Orientada a Objetos
- Responsabilidade única em classes
- Modularização do código
- Consumo de API REST
- Tratamento de exceções

---

## 🧠 Possíveis melhorias (roadmap)
- Buscar múltiplos CEPs via arquivo ``.txt``
- Salvar resultados em ``.csv`` ou ``.json``
- Histórico de buscas
- Interface de linha de comando com argparse ou typer
- Testes automatizados

---

## 📃 Licença
MIT. Pode usar, modificar e compartilhar livremente. Só não esquece de dar os créditos, né? 😄

---

## ✉️ Contato
Feito com 💻 e ☕ por **Tatyane Gonçalves**
[🔗 LinkedIn ](https://www.linkedin.com/in/tatyanegoncalves/) | [🐙 GitHub](https://github.com/Tatyane-Goncalves)