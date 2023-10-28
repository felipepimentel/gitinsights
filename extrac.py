from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://seusite.com')

        # Extração dos headers
        headers = await page.query_selector_all('[automation-col]')
        header_texts = []
        for header in headers:
            text = await header.eval_on_selector('span.title', 'el => el.textContent')
            header_texts.append(text)

        # Extração da sidebar
        sidebars = await page.query_selector_all('[automation-row]')
        sidebar_texts = []
        for sidebar in sidebars:
            text = await sidebar.eval_on_selector('span.title', 'el => el.textContent')
            sidebar_texts.append(text)

        # Extração do conteúdo
        cells = await page.query_selector_all('[data-col][data-row]')
        cell_values = []
        for cell in cells:
            text = await cell.inner_text()
            cell_values.append({
                'row': await cell.get_attribute('data-row'),
                'col': await cell.get_attribute('data-col'),
                'value': text
            })

        print('Headers:', header_texts)
        print('Sidebar:', sidebar_texts)
        print('Cell Values:', cell_values)

        await browser.close()

asyncio.run(main())
