import os
import shutil
from datetime import datetime
import time

# Defina o caminho para a pasta onde os screenshots estão armazenados
source_directory = 'caminho/para/a/pasta/de/screenshots'

# Dicionário para converter número do mês no nome por extenso
month_names = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março',
    4: 'Abril',   5: 'Maio',      6: 'Junho',
    7: 'Julho',   8: 'Agosto',    9: 'Setembro',
    10: 'Outubro',11: 'Novembro', 12: 'Dezembro'
}

def organize_screenshots(source_directory):
    # Lista todos os arquivos e subdiretórios no diretório de origem
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            try:
                # Construa o caminho completo para o arquivo atual
                file_path = os.path.join(root, file)

                # Pule pastas que já seguem o formato especificado (ano -> mês)
                if root.count(os.sep) - source_directory.count(os.sep) == 2:
                    try:
                        int(root.split(os.sep)[-2])  # Ano em formato numérico
                        datetime.strptime(root.split(os.sep)[-1], '%B')  # Mês por extenso
                        continue  # Este arquivo já está na pasta correta, pule
                    except (ValueError, IndexError):
                        pass

                # Use os metadados do arquivo para encontrar a data de modificação
                mtime = os.path.getmtime(file_path)
                year = datetime.fromtimestamp(mtime).year
                month = datetime.fromtimestamp(mtime).month

                # Defina o nome do diretório de destino com o ano e o mês por extenso
                dest_directory = os.path.join(source_directory, str(year), month_names[month])

                # Crie o diretório de destino se ele não existir
                os.makedirs(dest_directory, exist_ok=True)

                # Mova o arquivo para o diretório de destino
                shutil.move(file_path, os.path.join(dest_directory, file))
                print(f'Arquivo {file} movido para: {dest_directory}')
            except Exception as e:
                print(f'Erro ao organizar o arquivo {file}: {e}')

# Chama a função
organize_screenshots(source_directory)
