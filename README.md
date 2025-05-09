# ScrumBot 🤖📋

O **ScrumBot** é um agente inteligente baseado em LLMs que automatiza as primeiras etapas de planejamento ágil a partir de uma descrição de projeto. Ele gera:

- ✔️ Resumo do projeto
- 📋 Backlog do Produto (com PDF formatado)
- 🧩 Tarefas iniciais organizadas
- 📄 Logs detalhados de execução

---

## ✅ Requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com) instalado
- Sistema operacional compatível com Ollama (Windows/Mac/Linux)

---

## 🚀 Passo a Passo para Rodar o Projeto

### 1. Baixe e instale o Ollama

Acesse: https://ollama.com

Siga as instruções de instalação para seu sistema operacional.

---

### 2. Instale o modelo `llama3` no Ollama

Abra um terminal e execute:

```bash
ollama pull llama3
```

Mantenha o servidor do modelo ativo com:

```bash
ollama run llama3
```

> Esse comando deve rodar em **outro terminal** enquanto o ScrumBot estiver em uso.

---

### 3. Clone o projeto ou extraia o ZIP

```bash
cd scrumbot
```

---

### 4. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
```

Ative:

- No **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- No **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

---

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 6. Execute o ScrumBot

```bash
python main.py
```

Acesse no navegador:
```
http://127.0.0.1:7860
```

---

## 🗂 Estrutura básica

```
scrumbot/
├── main.py
├── tools/
├── prompts/
├── logs/
├── generated_backlogs/
├── requirements.txt
```

---

## 💡 Exemplo de uso

Você pode inserir a descrição do projeto diretamente ou enviar um arquivo `.pdf` com base no [modelo de projeto](Modelo_Projeto_ScrumBot.pdf).

O ScrumBot irá retornar:

- Resumo do projeto
- Backlog formatado
- Tarefas divididas
- Caminho para download do PDF

---

## 🧠 Desenvolvido com foco em produtividade ágil
Feito para equipes que desejam automatizar a fase inicial de planejamento com apoio de IA. Ideal para gerentes de projeto, product owners e squads ágeis.