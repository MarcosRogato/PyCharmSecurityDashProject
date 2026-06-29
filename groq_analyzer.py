from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def analisar_logs(logs):
    texto_log = ""
    for log in logs:
        texto_log += f"{log[1]} {log[2]} {log[3]} {log[4]} {log[5]}\n"

    prompt = f"""Você é um analista de segurança sênior especializado em detecção de intrusões.
Analise os logs abaixo e identifique:
1. IPs com comportamento suspeito
2. Padrões de ataque
3. Eventos críticos por prioridade: CRÍTICO, ALTO, MÉDIO, BAIXO

Responda em português de forma objetiva.

Logs:
{texto_log}"""

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Você é um analista de segurança sênior. Responda sempre em português, de forma clara e objetiva."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta.choices[0].message.content