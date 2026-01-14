from flask import Blueprint, render_template, url_for
import random
from pathlib import Path

# 1. Criamos um Blueprint. 
# O primeiro argumento ('main') é o nome do Blueprint.
# O segundo (__name__) diz ao Flask onde ele está localizado.
main_bp = Blueprint('main', __name__,
                    template_folder='templates', 
                    static_folder='static')

def get_random_image_from_folders():
    """Seleciona uma imagem aleatória da pasta cidades"""
    project_root = Path(__file__).parent.parent
    cidades_folder = project_root / "static" / "images" / "cidades"
    
    # Extensões de imagem aceitas
    image_extensions = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}
    all_images = []
    
    # Busca imagens na pasta cidades
    if cidades_folder.exists():
        for file in cidades_folder.iterdir():
            if file.is_file() and file.suffix in image_extensions:
                # Cria o caminho relativo para uso no template
                rel_path = file.relative_to(project_root / "static")
                all_images.append(str(rel_path).replace('\\', '/'))
    
    # Retorna uma imagem aleatória ou None
    if all_images:
        return random.choice(all_images)
    return None

# 2. Mudamos todas as @app.route para @main_bp.route
# E mudamos o nome da função 'index' para 'index_route' 
# (para evitar conflito de nomes, é uma boa prática)

@main_bp.route('/')
def index_route():
    # Seleciona uma imagem aleatória para o hero
    hero_image = get_random_image_from_folders()
    return render_template('index.html', 
                         active_page='index_route',
                         hero_image=hero_image)

@main_bp.route('/sobre')
def sobre_route():
    # Seleciona imagens aleatórias para hero interno e seção sobre
    hero_image = get_random_image_from_folders()
    sobre_image = get_random_image_from_folders()
    return render_template('sobre.html', 
                         active_page='sobre_route',
                         hero_image=hero_image,
                         sobre_image=sobre_image)

@main_bp.route('/membros')
def membros_route():
    # Seleciona uma imagem aleatória para o hero interno
    hero_image = get_random_image_from_folders()
    return render_template('membros.html', 
                         active_page='membros_route',
                         hero_image=hero_image)

@main_bp.route('/contato')
def contato_route():
    # Seleciona uma imagem aleatória para o hero interno
    hero_image = get_random_image_from_folders()
    return render_template('contato.html', 
                         active_page='contato_route',
                         hero_image=hero_image)