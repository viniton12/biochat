# biochat

 **📝 Premiação Melhores Projetos**

BioChat – Assistente Virtual de Biologia com Google Gemini
![image](https://github.com/user-attachments/assets/b19901cf-8bbe-4027-875f-ac2d622f2917)


# **🧬 Sobre o Projeto**
BioChat é um assistente virtual inteligente voltado para estudantes, professores e entusiastas de biologia que desejam automatizar tarefas comuns de estudo e pesquisa, utilizando a poderosa API do Google Gemini. O BioChat consegue identificar espécies em textos científicos, gerar resumos curtos e criar questionários de múltipla escolha, facilitando o aprendizado e a revisão do conteúdo.

Este projeto foi desenvolvido como parte da Imersão IA 2025, nas aulas 04 e 05, utilizando a API do Google Gemini para explorar processamento de linguagem natural em contexto educacional.

# **🚀 Funcionalidades**
Identificação automática de espécies em textos científicos de biologia.

Geração de resumos curtos para facilitar a compreensão rápida do conteúdo.

Criação de questionários de múltipla escolha para revisão e fixação do conteúdo.

Chat interativo que responde a comandos específicos e perguntas livres sobre biologia.

Uso obrigatório da Google API Key para autenticação e acesso ao modelo Gemini.

# **🛠 Tecnologias**
Python 3.8+

Biblioteca google.generativeai (Google Gemini API)

Ambiente recomendado: Google Colab, Jupyter Notebook, ou terminal local

Git & GitHub para versionamento e publicação do código

# **📋 Como Usar**
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seuusuario/biocchat.git
cd biocchat
Configure sua API Key do Google:

Obtenha sua chave em: Google Cloud Console

Defina a variável de ambiente GOOGLE_API_KEY no seu sistema ou insira diretamente no código (não recomendado para produção).

Instale as dependências:

bash
Copiar
Editar
pip install google-generativeai
Execute o programa:

bash
Copiar
Editar
python biochat.py
Use os comandos:

identifique espécie <texto> — para identificar espécies no texto.

gerar resumo <texto> — para criar resumos curtos.

gerar questionário <texto> — para criar perguntas de múltipla escolha.

Digite qualquer outra pergunta livre para interação geral.

Para sair, digite:

nginx
Copiar
Editar
sair
📂 Estrutura do Projeto
bash
Copiar
Editar
biocchat/
│
├── biochat.py          # Código principal do assistente
├── README.md           # Documentação do projeto
├── requirements.txt    # Lista de dependências
└── exemplos/           # Exemplos de textos para teste
    └── texto_teste.txt
    
# **📈 Exemplos de Uso**
less
Copiar
Editar
Você: identifique espécie A onça-pintada (Panthera onca) é um dos maiores felinos...
BioChat: A espécie mencionada é a onça-pintada (Panthera onca).

Você: gerar resumo A onça-pintada é um predador de topo na cadeia alimentar das Américas...
BioChat: A onça-pintada é um grande felino predador encontrado em florestas tropicais e cerrado.

Você: gerar questionário A onça-pintada tem pelagem com manchas em forma de rosetas...
BioChat:
1. Qual o nome científico da onça-pintada?
   a) Panthera leo
   b) Panthera onca
   c) Felis catus
   d) Puma concolor

2. Em quais habitats a onça-pintada é encontrada?
   a) Desertos
   b) Florestas tropicais e cerrado
   c) Ártico
   d) Oceanos

3. Qual é o papel da onça-pintada na cadeia alimentar?
   a) Herbívoro
   b) Produtor
   c) Predador de topo
   d) Decompositor
# **🎯 Objetivos**
Facilitar o estudo e a revisão de conteúdos em biologia.

Demonstrar o uso da API do Google Gemini em projetos reais.

Proporcionar uma experiência interativa e educativa para a comunidade.


