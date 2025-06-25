#  🚧 Projeto de Automação de Testes com Playwright + Pytest

Automação de testes para a página de login do site [Serverest Front](https://front.serverest.dev/login), utilizando **Playwright** com **Pytest** e arquitetura baseada em **Page Object Model (POM)**.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)

---

## 📁 Estrutura de Pastas

```
teste_playwright/
│
├── tests/
│   └── test_login.py           # Testes automatizados
│
├── pages/
│   ├── base_page.py            # Página base com utilitários comuns
│   └── login_page.py           # Page Object da tela de login
│
├── conftest.py                 # Fixtures do Pytest (browser, página etc.)
├── pytest.ini                  # Configurações do Pytest
└── requirements.txt            # Dependências do projeto
```

---

## ⚙️ Instalação do Ambiente

1. Clone o projeto:
   ```bash
   git clone https://github.com/eliasramiresjr/teste_playwright
   cd teste_playwright
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Executando os Testes

```bash
pytest
```

Ou para rodar um teste específico:

```bash
pytest tests/test_login.py
```


---

## 📌 Melhorias Futuras

- Testes com dados inválidos
- Suporte a Allure Reports
- Execução paralela com `pytest-xdist`
- Integração com CI/CD (GitHub Actions, GitLab CI etc.)
