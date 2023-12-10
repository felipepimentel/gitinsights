import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def extract_form_data(page, form_selector):
    # Esperar pelo carregamento completo da página
    await page.wait_for_load_state('networkidle')

    # Obter todos os elementos de entrada do formulário
    input_elements = await page.query_selector_all(f'{form_selector} input')
    select_elements = await page.query_selector_all(f'{form_selector} select')
    textarea_elements = await page.query_selector_all(f'{form_selector} textarea')

    # Dicionário para armazenar os dados do formulário
    form_data = {}

    # Extrair dados dos inputs
    for element in input_elements:
        element_type = await element.get_attribute('type')
        element_name = await element.get_attribute('name') or await element.get_attribute('id')
        if element_type == 'checkbox' or element_type == 'radio':
            value = await element.is_checked()
        else:
            value = await element.input_value()
        form_data[element_name] = value

    # Extrair dados dos selects
    for element in select_elements:
        element_name = await element.get_attribute('name') or await element.get_attribute('id')
        value = await element.input_value()
        form_data[element_name] = value

    # Extrair dados dos textareas
    for element in textarea_elements:
        element_name = await element.get_attribute('name') or await element.get_attribute('id')
        value = await element.input_value()
        form_data[element_name] = value

    # Converter para DataFrame
    df = pd.DataFrame([form_data])

    return df

async def main():
    # Inicializar o Playwright e abrir uma nova página
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Navegar até a página com o formulário
        await page.goto('URL_DO_SEU_FORMULÁRIO')

        # Extrair os dados do formulário
        form_selector = 'SELETOR_DO_SEU_FORMULÁRIO'  # Substitua com o seletor CSS correto
        df = await extract_form_data(page, form_selector)
        
        # Imprimir os dados do formulário
        print(df)

        # Fechar o navegador
        await browser.close()

# Executar o script
asyncio.run(main())
