from playwright.async_api import async_playwright

async def extract_data_labels(page):
    # Localize todos os elementos com data-type=label
    data_labels = page.locator('[data-type="label"]')
    results = []

    # Conta o número de elementos encontrados
    count = await data_labels.count()
    
    # Itera sobre os elementos encontrados
    for i in range(count):
        # Localize o elemento label dentro do div com data-type=label
        label = await data_labels.nth(i).locator("label[for]").first()
        
        # Captura o texto do label
        text = await label.inner_text()
        
        # Captura o valor do atributo 'for'
        for_value = await label.get_attribute("for")
        
        # Use o valor de 'for' para localizar o elemento correspondente e obter o seu valor
        element_for = await page.locator(f"#{for_value}").first()
        element_value = ""
        if await element_for.count() > 0:  # Verifica se o elemento existe
            element_value = await element_for.input_value()

        # Adiciona os resultados em uma lista
        results.append({
            "for": for_value,
            "text": text.strip(),
            "value": element_value
        })
    
    return results

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')  # Substitua pela URL da sua página

        data = await extract_data_labels(page)
        print(data)  # Imprime o resultado ou faz outra operação desejada

        await browser.close()

import asyncio
asyncio.run(main())
