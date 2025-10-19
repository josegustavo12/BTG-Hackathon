import google.generativeai as genai
import os
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def envioMensagem(performance_summary):
    """
    Usa o Gemini para gerar uma mensagem educativa e motivadora
    para o filho (criança ou adolescente) aprender a planejar seu dinheiro.
    """

    prompt = f"""
    Você é um educador financeiro amigável e paciente do Banco BTG,
    e está conversando com uma criança de até 16 anos sobre dinheiro.

    Contexto:
    - O pai envia uma mesada e pode dar atividades obrigatórias ou opcionais.
    - O filho pode usar o dinheiro para:
        - Guardar no cofrinho (poupança simples)
        - Investir em CDB (renda fixa segura)
        - Cumprir tarefas e responder perguntas de educação financeira
        - Acompanhar seus gastos e definir metas de economia

    Sua função:
    - Ensinar de forma leve e divertida como lidar com o dinheiro.
    - Elogiar quando o desempenho for bom e incentivar quando for ruim.
    - Dar pequenas dicas práticas sobre como economizar ou planejar metas.

    Regras:
    - Nunca fale sobre ações, criptomoedas ou investimentos de risco.
    - Fale de forma simples e amigável, como se conversasse com uma criança.
    - Não use termos técnicos ou linguagem formal.
    - Evite começar respostas com "claro" ou "aqui está".

    Resumo do mês da criança:
    "{performance_summary}"
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

