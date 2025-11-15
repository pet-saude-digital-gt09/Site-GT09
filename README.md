# Portal GT-09: Interoperabilidade e Parcerias no SUS Digital

O portal serve como um ponto central para apresentar a missão do grupo, seus membros, objetivos e informações de contato.

---

## 🚀 Funcionalidades
O site é composto pelas seguintes páginas:

- Página Inicial: Apresenta o grupo e seus objetivos principais.

- Sobre o GT-09: Detalha a missão, visão e os objetivos estratégicos.

- Membros: Apresenta a equipe dividida em Coordenadoras, Preceptoras e Monitores.

- Contato: Lista os canais de comunicação, e-mail e redes sociais.

## 🛠️ Tecnologias Utilizadas
Este projeto foi construído utilizando as seguintes tecnologias:

- Back-end:

  - Python

  - Flask: Um micro-framework para o servidor web e gerenciamento de rotas.

- Front-end:

  - HTML5

  - CSS3 (para estilização)

  - Jinja2: O motor de templates do Flask, usado para integrar o Python ao HTML.

- Fontes e Ícones:

  - Google Fonts (Montserrat e Open Sans)

  - Font Awesome (para ícones)

## 📁 Estrutura do Projeto
A estrutura de pastas está organizada da seguinte forma, seguindo as convenções do Flask:

```
seu-projeto/

│
├── app.py                 # Arquivo principal do Flask (servidor)
│
├── main_routes/
│   └── routes.py          # (Onde as rotas do site são definidas)
│
├── static/                # Arquivos públicos (CSS, imagens, JS)
│   ├── style.css          # Folha de estilos principal
│   ├── logo.png           # Logo do site (usado na barra de navegação)
│   └── images/            # Fotos dos membros
│       ├── ClaudiaMelo.png
│       ├── EgmarLongo.png
│       ├── AnnaMel.png
│       └── ...
│
└── templates/             # Arquivos HTML com Jinja2
    ├── base.html          # Template base (menu, footer)
    ├── index.html         # Página inicial
    ├── sobre.html         # Página 'Sobre'
    ├── membros.html       # Página 'Membros'
    └── contato.html       # Página 'Contato'
```

## ⚙️ Como Executar (Ambiente de Desenvolvimento)
Para rodar este projeto localmente no seu computador, siga os passos abaixo.

Pré-requisitos
- Python 3.x

- pip (gerenciador de pacotes do Python)

Instalação
1. Clone o repositório:
  
    ```
    Bash
    
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. (Recomendado) Crie e ative um ambiente virtual:

- No macOS/Linux:

  ```
  Bash
  
  python3 -m venv venv
  source venv/bin/activate
  ```

- No Windows:

  ```
  Bash
  
  python -m venv venv
  .\venv\Scripts\activate
  ```

- Instale as dependências (o Flask):
    ```
    Bash
    
    pip install Flask
    ```

- Rodando o Servidor
1. Com o ambiente virtual ativado e as dependências instaladas, execute o arquivo app.py:

    ```
    Bash
    
    python app.py
    ```

2. O servidor de desenvolvimento será iniciado. Você verá uma mensagem similar a esta:
    ```
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```

3. Abra o seu navegador e acesse http://127.0.0.1:5000/ para ver o site.
