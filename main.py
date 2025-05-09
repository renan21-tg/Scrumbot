import gradio as gr
import time
import os
from datetime import datetime
from ollama_agent import call_ollama
from tools.backlog_pdf_writter import generate_backlog_pdf

def load_prompt(file, content):
    with open(f"prompts/{file}", "r", encoding="utf-8") as f:
        return f.read().replace("{conteudo}", content)

def save_log(entry, resumo, backlog, tarefas, duration):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"""
==================== {timestamp} ====================
📥 Entrada:
{entry}

📄 Resumo:
{resumo.strip()}

🧾 Backlog:
{backlog.strip()}

🧩 Tarefas:
{tarefas.strip()}

⏱ Tempo de processamento: {duration:.2f} segundos
=====================================================

"""
    os.makedirs("logs", exist_ok=True)
    with open("logs/history.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_content)

def parse_backlog_to_items(text):
    """
    Espera linhas no formato:
    High | User Story: ...
    """
    lines = [line.strip() for line in text.strip().split("\n") if "User Story:" in line]
    items = []
    prioridade_map = {
        "High": "High",
        "Medium": "Medium",
        "Low": "Low"
    }

    for idx, line in enumerate(lines, 1):
        try:
            parts = line.split("|")
            prioridade_raw = parts[0].strip()
            prioridade = prioridade_map.get(prioridade_raw, prioridade_raw)
            user_story = parts[1].split(":", 1)[1].strip()

            items.append({
                "id": idx,
                "prioridade": prioridade,
                "user_story": user_story
            })
        except Exception:
            continue

    return items

def process_input(description):
    start = time.time()

    resumo = call_ollama(load_prompt("summarize.txt", description))
    backlog = call_ollama(load_prompt("generate_backlog_items.txt", description))
    tarefas = call_ollama(load_prompt("split_tasks.txt", description))

    backlog_items = parse_backlog_to_items(backlog)
    pdf_path = generate_backlog_pdf(backlog_items)

    duration = time.time() - start
    save_log(description, resumo, backlog, tarefas, duration)

    return resumo, backlog, tarefas, f"PDF saved in: {pdf_path}"

iface = gr.Interface(
    fn=process_input,
    inputs=gr.Textbox(label="Project Description", lines=10),
    outputs=[
        gr.Textbox(label="Project Summary"),
        gr.Textbox(label="Product Backlog"),
        gr.Textbox(label="Task Breakdown"),
        gr.Textbox(label="Backlog PDF Path"),
    ],
    title="ScrumBot"
)

if __name__ == "__main__":
    iface.launch()