from playwright.sync_api import sync_playwright
import requests

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Faça o login e navegue até a página desejada aqui
        # ...

        # Obter os cookies
        cookies = page.context.cookies()

        browser.close()

        # Preparar o dicionário de cookies para usar com requests
        cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

        # Agora você pode usar esses cookies com as suas requisições HTTP
        # Exemplo:
        response = requests.get("https://example.com/alguma_pagina", cookies=cookies_dict)
        print(response.text)

if __name__ == "__main__":
    main()




from playwright.sync_api import sync_playwright
import requests

def get_ajax_request_details(page):
    # Captura a primeira requisição AJAX que corresponde aos critérios
    with page.expect_request("**/*url_da_requisicao*") as request_info:
        page.click("seletor_do_botao_para_carregar_dados")  # ou alguma ação que dispara a requisição
    request = request_info.value
    return request

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Fazer login
        page.goto("https://example.com/login")
        # preencher credenciais e submeter o formulário de login
        # ...

        # Navegar até o relatório
        page.goto("https://example.com/relatorio")

        # Capturar detalhes da requisição AJAX
        ajax_request = get_ajax_request_details(page)

        # Agora você tem os detalhes da requisição AJAX
        url = ajax_request.url
        method = ajax_request.method
        headers = ajax_request.headers
        # Em caso de POST, pegar o corpo da requisição
        post_data = ajax_request.post_data if method == "POST" else None

        # Fazer requisições para outras páginas
        for i in range(2, total_de_paginas + 1):
            # Modificar parâmetros conforme necessário
            if post_data:
                post_data["page"] = i
                response = requests.post(url, headers=headers, json=post_data)
            else:
                response = requests.get(f"{url}?page={i}", headers=headers)
            
            if response.status_code == 200:
                dados = response.json()
                # Processar os dados
                print(dados)
            else:
                print(f"Erro na requisição da página {i}: {response.status_code}")

        browser.close()

if __name__ == "__main__":
    main()


import requests

# Detalhes da requisição capturados pelas ferramentas do desenvolvedor
url = "https://example.com/api/data"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer seu_token_aqui",
    # Inclua outros cabeçalhos necessários
}
data = {
    # Dados necessários para a requisição (se for um método POST, por exemplo)
}

# Fazendo a requisição
response = requests.get(url, headers=headers, json=data)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Processar a resposta
    dados = response.json()
    print(dados)
else:
    print(f"Erro na requisição: {response.status_code}")


from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")

        # Substitua o seletor abaixo com o seletor específico para o script desejado
        script_element = page.query_selector("seletor_do_script")

        if script_element:
            script_content = script_element.inner_text()  # ou .inner_html() dependendo do caso
            print(script_content)
        else:
            print("Elemento script não encontrado.")

        browser.close()

if __name__ == "__main__":
    main()


import re

# Aqui está uma simulação de como seria o script que você forneceu como imagem
script_content = """
// ... [outro código] ...
list.setListControlID('algum_valor');
list.setProperties('H45IAAAAAAAAAIX28XnbSxK...continuação...query string');
// ... [mais código] ...
"""

# Expressão regular que procura por 'setProperties' que segue um 'setListControlID'
pattern = r"setListControlID\('.*?'\);\s*list\.setProperties\('([^']*)'"

# Pesquisar no conteúdo do script
match = re.search(pattern, script_content, re.DOTALL)
if match:
    valor_desejado = match.group(1)
    print(valor_desejado)
else:
    print("Valor não encontrado no script.")
import re
from playwright.sync_api import sync_playwright

# Inicializar Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Ir até a página desejada
    page.goto('https://example.com/determinada_pagina')
    
    # Login, se necessário
    # page.fill('input[name="username"]', 'seu_usuario')
    # page.fill('input[name="password"]', 'sua_senha')
    # page.click('button[type="submit"]')
    # page.wait_for_navigation()

    # Capturar o primeiro request XHR com a query string específica
    with page.expect_request("**/*list-people*") as first_request_info:
        page.wait_for_load_state('networkidle')
    first_request = first_request_info.value

    # Se necessário, interaja com a página aqui para induzir o request XHR
    
    # Analisar o HTML e os scripts JavaScript para montar as requests subsequentes
    # Exemplo para obter o conteúdo do script:
    script_content = page.content()
    pattern = r"setListControlID\('.*?'\);\s*list\.setProperties\('([^']*)'"
    match = re.search(pattern, script_content, re.DOTALL)
    if match:
        valor_desejado = match.group(1)
        print(valor_desejado)
    
    # Realizar requests POST para as próximas páginas
    # Supondo que 'valor_desejado' é parte da informação necessária para a próxima request
    import requests
    for page_number in range(2, 100):  # Um número arbitrário para limitar as páginas
        data = {
            # Incluir dados necessários para a requisição POST aqui
            # 'algumCampo': valor_desejado, 'page': page_number, ...
        }
        response = requests.post(first_request.url, json=data)
        if response.status_code == 404:
            print(f"Página {page_number} não encontrada, terminando a navegação.")
            break
        elif response.ok:
            # Processar a resposta
            print(f"Dados da página {page_number} recebidos.")
        else:
            print(f"Erro na página {page_number}: {response.status_code}")

    browser.close()
