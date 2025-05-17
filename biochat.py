# Instale a biblioteca (execute esta célula primeiro no Colab)
!pip install google-generativeai --quiet

import os
import google.generativeai as genai
from IPython.display import display, clear_output
import ipywidgets as widgets

# CONFIGURE SUA API KEY AQUI
os.environ["GOOGLE_API_KEY"] = ""  # <-- substitua aqui

# Configurar Gemini
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
modelo = genai.GenerativeModel("gemini-2.0-flash")

def identificar_especie(texto):
    if not texto.strip():
        return "Por favor, insira um texto válido para identificar a espécie."
    prompt = f"Identifique a espécie mencionada neste texto de biologia: '{texto}'"
    try:
        resposta = modelo.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Erro ao identificar espécie: {e}"

def gerar_resumo(texto):
    if not texto.strip():
        return "Por favor, insira um texto válido para gerar o resumo."
    prompt = f"Faça um resumo curto do seguinte texto de biologia:\n{texto}"
    try:
        resposta = modelo.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Erro ao gerar resumo: {e}"

def gerar_questionario(texto):
    if not texto.strip():
        return "Por favor, insira um texto válido para gerar o questionário."
    prompt = f"Crie 3 perguntas de múltipla escolha baseadas neste texto de biologia:\n{texto}"
    try:
        resposta = modelo.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Erro ao gerar questionário: {e}"

# Widgets
entrada = widgets.Textarea(
    value='',
    placeholder='Digite seu texto de biologia aqui...',
    description='Texto:',
    layout=widgets.Layout(width='80%', height='150px')
)

opcoes = widgets.RadioButtons(
    options=[
        ('Identificar espécie', 'identificar'),
        ('Gerar resumo', 'resumo'),
        ('Gerar questionário', 'questionario')
    ],
    description='Ação:',
    disabled=False
)

botao = widgets.Button(description="Executar")

saida = widgets.Output(layout=widgets.Layout(border='1px solid black', padding='10px', width='80%', height='150px'))

def ao_clicar(b):
    with saida:
        clear_output()
        texto = entrada.value
        acao = opcoes.value
        print("Processando...\n")
        
        if acao == 'identificar':
            resultado = identificar_especie(texto)
        elif acao == 'resumo':
            resultado = gerar_resumo(texto)
        elif acao == 'questionario':
            resultado = gerar_questionario(texto)
        else:
            resultado = "Ação desconhecida."

        print(resultado)

botao.on_click(ao_clicar)

display(widgets.VBox([entrada, opcoes, botao, saida]))
