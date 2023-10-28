from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://seusite.com')

        # Encontre todas as tabelas pela classe ou algum atributo distintivo
        tabelas = await page.query_selector_all('div[custom-title][custom-id]')
        
        for tabela in tabelas:
            categoria = await tabela.get_attribute('custom-title')

            # Extração de headers, sidebar e content como anteriormente
            headers = await tabela.query_selector_all('[automation-col]')
            sidebars = await tabela.query_selector_all('[automation-row]')
            cells = await tabela.query_selector_all('[data-col][data-row]')
            
            # ... (processamento similar ao do código anterior)
            
            # Persistência no banco de dados
            for header, sidebar, cell in zip(headers, sidebars, cells):
                header_text = await header.inner_text()
                sidebar_text = await sidebar.inner_text()
                cell_text = await cell.inner_text()
                
                registro = Tabela(
                    categoria=categoria,
                    indicador=sidebar_text,
                    data=header_text,
                    valor=float(cell_text)  # Supondo que o valor é um float; ajuste conforme necessário
                )
                
                session.add(registro)

            # Commit das alterações ao banco de dados
            session.commit()

        await browser.close()

asyncio.run(main())
