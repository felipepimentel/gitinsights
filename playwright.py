import yaml
import re

# Regex para identificar variáveis no formato $(variavel)
variable_regex = re.compile(r'\$\((\w+)\)')

# Função para substituir as variáveis
def replace_variables(yaml_content, variable_values):
    # Substituir todas as ocorrências das variáveis
    def replace(match):
        variable_name = match.group(1)
        if variable_name in variable_values:
            return variable_values[variable_name]
        else:
            raise ValueError(f"Variable '{variable_name}' not defined.")
    return variable_regex.sub(replace, yaml_content)

# Função para carregar o YAML e substituir as variáveis
def load_and_process_yaml(file_path, variable_values):
    with open(file_path, 'r') as file:
        yaml_content = file.read()
    
    # Substituir as variáveis
    try:
        processed_content = replace_variables(yaml_content, variable_values)
        return yaml.safe_load(processed_content)
    except ValueError as e:
        print(e)
        return None

# Caminho para o arquivo YAML
file_path = 'path/to/your/yaml/file.yaml'

# Dicionário com os valores das variáveis
variable_values = {
    'variavel1': 'valor1',
    'variavel2': 'valor2',
    # Adicione suas variáveis e valores aqui
}

# Processar o YAML
processed_yaml = load_and_process_yaml(file_path, variable_values)
if processed_yaml:
    print(processed_yaml)
