import os
import shutil
from datetime import datetime

# Diretório que contém os screenshots
root_dir = '/caminho/para/a/pasta/com/screenshots'

# Formatos de arquivo a serem considerados como screenshots
file_extensions = ['.png', '.jpg', '.jpeg']

def organize_screenshots(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # Checa se o arquivo é um screenshot
            if any(file.lower().endswith(ext) for ext in file_extensions):
                file_path = os.path.join(subdir, file)

                # Obter a data de criação do arquivo
                creation_time = os.path.getctime(file_path)
                date_folder_name = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')

                # Criar um diretório para a data se ele não existir
                dest_dir = os.path.join(directory, date_folder_name)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                # Mover o arquivo para o diretório correspondente
                shutil.move(file_path, os.path.join(dest_dir, file))
                print(f"Arquivo {file} movido para: {dest_dir}")

# Chama a função para organizar os screenshots
organize_screenshots(root_dir)
