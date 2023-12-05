import pandas as pd
from bs4 import BeautifulSoup

def html_form_to_data_frame(content, form_id):
    soup = BeautifulSoup(content, "html.parser")
    form = soup.find('form', id=form_id)
    if not form:
        raise ValueError(f"Form with id {form_id} not found")
    
    data = []
    # Extrai todos os elementos de input, textarea e select
    for element in form.find_all(['input', 'textarea', 'select']):
        element_id = element.get('id')
        label = soup.find('label', {'for': element_id})
        label_text = label.get_text(strip=True) if label else ""
        
        # Trata diferentes tipos de elementos de entrada
        if element.name == 'input':
            input_type = element.get('type', 'text')
            if input_type in ['checkbox', 'radio']:
                value = element.get('checked')
            else:
                value = element.get('value')
        elif element.name == 'textarea':
            value = element.text
        elif element.name == 'select':
            selected_option = element.find('option', selected=True)
            value = selected_option.get('value') if selected_option else None
        
        data.append({"label": label_text, "value": value})
    
    df = pd.DataFrame(data)
    return df

# Exemplo de uso:
# content = seu_html_aqui
# form_id = 'seu_form_id_aqui'
# df = html_form_to_data_frame(content, form_id)
# print(df)
