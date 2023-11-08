import json
import os

# Nome do arquivo de controle
control_file = 'process_control.json'

def load_control_state():
    # Carrega o estado de controle se o arquivo existir, senão, retorna um dicionário vazio
    if os.path.exists(control_file):
        with open(control_file, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_control_state(state):
    # Salva o estado de controle atual no arquivo JSON
    with open(control_file, 'w') as f:
        json.dump(state, f, indent=4)

def update_control_state(module, class_name, name, executed):
    # Atualiza o estado de controle para um determinado processo
    state = load_control_state()
    key = f"{module}#{class_name}#{name}"
    state[key] = {'executed': executed}
    save_control_state(state)

def check_if_executed(module, class_name, name):
    # Verifica se um determinado processo já foi executado
    state = load_control_state()
    key = f"{module}#{class_name}#{name}"
    return state.get(key, {}).get('executed', False)

# Exemplo de como usar as funções acima
module = 'meu_modulo'
class_name = 'MinhaClasse'
name = 'nome_da_operacao'

# Verificar se o processo já foi executado
if not check_if_executed(module, class_name, name):
    try:
        # Executar processo
        # ...
        # Atualizar o estado como executado se o processo for concluído com sucesso
        update_control_state(module, class_name, name, True)
    except Exception as e:
        # Lidar com a exceção, log, etc.
        # Não atualiza o estado, para que o processo seja tentado novamente
        print(f"Erro: {e}")
