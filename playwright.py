from playwright.async_api import async_playwright
import asyncio
import json

async def extract_hierarchy(page, selector):
    elements = await page.query_selector_all(f'{selector} > *')  # Seleciona todos os elementos filhos diretos da div
    hierarchy = []

    for element in elements:
        tag_name = await element.evaluate('element => element.tagName')
        label = await element.evaluate("""(element) => {
            let label = element.querySelector('label');
            return label ? label.innerText : '';
        }""")
        children = await extract_hierarchy(element, '> *')  # Recursivamente obtém a hierarquia dos filhos
        hierarchy.append({
            'tag': tag_name,
            'label': label.strip(),
            'children': children
        })

    return hierarchy

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://your-page-url.com')
        
        # Suponha que a div que você quer inspecionar tem um id 'my-div'
        data = await extract_hierarchy(page, '#my-div')
        print(json.dumps(data, indent=2))
        
        await browser.close()

asyncio.run(main())
