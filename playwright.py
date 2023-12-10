import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import json

async def extract_form_data(page, form_selector):
    form_data = []

    # Selecione todos os elementos de entrada dentro do formulário
    input_elements = await page.query_selector_all(f"{form_selector} input, {form_selector} textarea, {form_selector} select")
    
    # Itere por cada elemento para extrair dados
    for element in input_elements:
        element_tag_name = await page.evaluate('(element) => element.tagName', element)
        name_or_id = await page.evaluate('(element) => element.name || element.id', element)
        label = await page.query_selector(f"label[for='{name_or_id}']")
        label_text = await label.inner_text() if label else name_or_id  # Usa o ID ou o nome como backup se a label não existir
        
        if element_tag_name == 'SELECT':
            value = await page.evaluate('(element) => element.options[element.selectedIndex].value', element)
        elif element_tag_name == 'INPUT':
            type_attr = await page.evaluate('(element) => element.type', element)
            if type_attr == 'checkbox' or type_attr == 'radio':
                value = await page.evaluate('(element) => element.checked', element)
            else:
                value = await page.evaluate('(element) => element.value', element)
        elif element_tag_name == 'TEXTAREA':
            value = await page.evaluate('(element) => element.value', element)
        else:
            continue  # Pule elementos que não são reconhecidos
        
        form_data.append({"label": label_text, "value": value})
    
    # Converta a lista de dicionários para uma string JSON
    json_content = json.dumps(form_data)
    
    # Crie um DataFrame com a coluna content contendo a string JSON
    df = pd.DataFrame([{"content": json_content}])
    return df

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto('sua_url_do_formulário')
        
        # Substitua 'seu_seletor_de_formulário' pelo seletor CSS do seu formulário
        data_frame = await extract_form_data(page, 'seu_seletor_de_formulário')
        
        print(data_frame.to_string(index=False))  # Mostra o DataFrame sem o índice

        await browser.close()

asyncio.run(main())
