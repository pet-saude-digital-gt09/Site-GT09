"""
Script para organizar as imagens do MTur baixadas
Localiza as pastas 'paraiba' e 'cabedelo' e organiza as imagens no formato correto
"""

import os
import shutil
import random
from pathlib import Path

# Caminhos
PROJECT_ROOT = Path(__file__).parent
TARGET_DIR = PROJECT_ROOT / "static" / "images" / "paraiba"

# Nomes dos arquivos necessários
REQUIRED_FILES = {
    "hero-paraiba.jpg": {
        "description": "Hero da página inicial (1920x600px recomendado)",
        "preferred_keywords": ["praia", "paisagem", "vista", "aerea", "cidade", "coast", "beach"]
    },
    "hero-interno-paraiba.jpg": {
        "description": "Hero das páginas internas (1920x400px recomendado)",
        "preferred_keywords": ["paisagem", "urbana", "cidade", "arquitetura", "centro"]
    },
    "sobre-paraiba.jpg": {
        "description": "Imagem da página Sobre (600x400px recomendado)",
        "preferred_keywords": ["paisagem", "cultura", "turismo", "ponto", "turistico"]
    }
}

def find_image_folders():
    """Procura pelas pastas 'paraiba' e 'cabedelo' no projeto"""
    possible_locations = [
        PROJECT_ROOT,
        PROJECT_ROOT.parent,
        PROJECT_ROOT / "Downloads",
        Path.home() / "Downloads",
        Path.home() / "Desktop"
    ]
    
    folders = {}
    for location in possible_locations:
        if not location.exists():
            continue
            
        # Procura por 'paraiba' e 'cabedelo'
        for item in location.iterdir():
            if item.is_dir():
                name_lower = item.name.lower()
                if 'paraiba' in name_lower and 'paraiba' not in folders:
                    folders['paraiba'] = item
                elif 'cabedelo' in name_lower and 'cabedelo' not in folders:
                    folders['cabedelo'] = item
    
    return folders

def get_image_files(folder):
    """Lista todos os arquivos de imagem em uma pasta"""
    image_extensions = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}
    images = []
    
    if not folder.exists():
        return images
    
    for file in folder.iterdir():
        if file.is_file() and file.suffix in image_extensions:
            images.append(file)
    
    return images

def score_image(filename, keywords):
    """Dá uma pontuação para uma imagem baseada nas palavras-chave preferidas"""
    filename_lower = filename.lower()
    score = 0
    
    for keyword in keywords:
        if keyword.lower() in filename_lower:
            score += 1
    
    return score

def select_best_image(images, keywords, min_width=None):
    """Seleciona a melhor imagem baseada em palavras-chave"""
    if not images:
        return None
    
    scored_images = []
    
    for img_path in images:
        score = score_image(img_path.name, keywords)
        
        scored_images.append({
            'path': img_path,
            'score': score
        })
    
    # Ordena por score (maior primeiro)
    scored_images.sort(key=lambda x: x['score'], reverse=True)
    
    return scored_images[0]['path'] if scored_images else images[0]

def copy_and_rename_image(source, target_name):
    """Copia e renomeia uma imagem"""
    target_path = TARGET_DIR / target_name
    
    # Garante que o diretório existe
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    
    # Copia o arquivo (mantém o formato original)
    shutil.copy2(source, target_path)
    
    return target_path

def main():
    print("=" * 70)
    print("Organizador de Imagens do MTur - GT-09")
    print("=" * 70)
    
    # Procura pelas pastas
    print("\n🔍 Procurando pastas com imagens...")
    folders = find_image_folders()
    
    if not folders:
        print("\n❌ Não foram encontradas as pastas 'paraiba' ou 'cabedelo'.")
        print("\nPor favor, informe onde estão as pastas:")
        print("1. Coloque as pastas na raiz do projeto (mesmo nível que app.py)")
        print("2. Ou coloque na pasta Downloads")
        print("3. Ou execute este script novamente após mover as pastas")
        return
    
    print(f"\n✓ Pastas encontradas:")
    for name, path in folders.items():
        print(f"  - {name}: {path}")
    
    # Coleta todas as imagens
    all_images = {}
    for folder_name, folder_path in folders.items():
        images = get_image_files(folder_path)
        all_images[folder_name] = images
        print(f"\n📸 Imagens em '{folder_name}': {len(images)} arquivos")
    
    if not any(all_images.values()):
        print("\n❌ Nenhuma imagem encontrada nas pastas!")
        return
    
    # Garante que o diretório de destino existe
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "=" * 70)
    print("Selecionando e organizando imagens...")
    print("=" * 70)
    
    # Seleciona imagens aleatórias (sem repetir)
    selected_images = {}
    
    # Coleta todas as imagens em uma lista única
    all_images_flat = []
    for folder_name, images in all_images.items():
        all_images_flat.extend(images)
    
    if not all_images_flat:
        print("\n❌ Nenhuma imagem disponível para selecionar!")
        return
    
    # Cria uma cópia da lista para não modificar a original
    available_images = all_images_flat.copy()
    random.shuffle(available_images)  # Embaralha as imagens
    
    for target_name, config in REQUIRED_FILES.items():
        print(f"\n📋 {target_name}")
        print(f"   {config['description']}")
        
        # Seleciona uma imagem aleatória (sem repetir)
        if available_images:
            selected_image = available_images.pop(0)  # Pega a primeira da lista embaralhada
            # Encontra de qual pasta veio
            source_folder = None
            for folder_name, images in all_images.items():
                if selected_image in images:
                    source_folder = folder_name
                    break
            
            print(f"   ✓ Selecionada aleatoriamente: {selected_image.name} (de {source_folder})")
            selected_images[target_name] = selected_image
        else:
            print(f"   ⚠️  Nenhuma imagem disponível (todas já foram usadas)")
    
    # Copia e renomeia as imagens
    print("\n" + "=" * 70)
    print("Copiando imagens para o destino...")
    print("=" * 70)
    
    for target_name, source_path in selected_images.items():
        try:
            result_path = copy_and_rename_image(source_path, target_name)
            print(f"✓ {target_name} ← {source_path.name}")
        except Exception as e:
            print(f"❌ Erro ao copiar {target_name}: {e}")
    
    # Verifica quais arquivos ainda faltam
    print("\n" + "=" * 70)
    print("Resumo:")
    print("=" * 70)
    
    missing = []
    for target_name in REQUIRED_FILES.keys():
        target_path = TARGET_DIR / target_name
        if target_path.exists():
            print(f"✓ {target_name}")
        else:
            print(f"❌ {target_name} - FALTANDO")
            missing.append(target_name)
    
    if missing:
        print(f"\n⚠️  {len(missing)} imagem(ns) ainda faltando.")
        print("\nVocê pode:")
        print("1. Executar este script novamente (ele tentará selecionar outras imagens)")
        print("2. Copiar manualmente as imagens para:")
        print(f"   {TARGET_DIR}")
        print("3. Renomear as imagens manualmente para os nomes corretos")
    else:
        print("\n🎉 Todas as imagens foram organizadas com sucesso!")
        print(f"\nAs imagens estão em: {TARGET_DIR}")
        print("\nVocê pode agora executar o servidor Flask para ver o resultado!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
