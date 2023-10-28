from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import re  # para expressão regular

# ... (Código SQLAlchemy para configuração do banco de dados)

async def main():
    # ... (Código Playwright para navegar até a página)

    # Encontre todas as tabelas pela classe ou algum atributo distintivo
    tabelas = await page.query_selector_all('div[custom-title][custom-id]')
    
    for tabela in tabelas:
        categoria = await tabela.get_attribute('custom-title')

        # Encontrar headers e sidebars
        headers = await tabela.query_selector_all('[cell-template^="data-col-"]')
        sidebars = await tabela.query_selector_all('[cell-template^="data-row-"]')
        cells = await tabela.query_selector_all('[data-col][data-row]')
        
        header_dict = {}
        sidebar_dict = {}
        
        for header in headers:
            attr_value = await header.get_attribute('cell-template')
            col_index = int(re.search(r'data-col-(\d+)', attr_value).group(1))
            header_text = await header.inner_text()
            header_dict[col_index] = header_text
            
        for sidebar in sidebars:
            attr_value = await sidebar.get_attribute('cell-template')
            row_index = int(re.search(r'data-row-(\d+)', attr_value).group(1))
            sidebar_text = await sidebar.inner_text()
            sidebar_dict[row_index] = sidebar_text
        
        for cell in cells:
            col_index = int(await cell.get_attribute('data-col'))
            row_index = int(await cell.get_attribute('data-row'))
            cell_text = await cell.inner_text()
            
            registro = Tabela(
                categoria=categoria,
                indicador=sidebar_dict.get(row_index, "Desconhecido"),
                data=header_dict.get(col_index, "Desconhecido"),
                valor=float(cell_text)  # Supondo que o valor é um float; ajuste conforme necessário
            )
            
            session.add(registro)
        
        # Commit das alterações ao banco de dados
        session.commit()

    await browser.close()

# Executa a função assíncrona
asyncio.run(main())
