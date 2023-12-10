import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def extract_form_data(page, form_selector):
    # Select all input elements within the form
    input_elements = await page.query_selector_all(f'{form_selector} input')
    
    form_data = []
    
    # Iterate through each input element to extract data
    for input_element in input_elements:
        # Depending on the structure of your form you might need to adjust the selectors
        label = await page.evaluate(f'(element) => document.querySelector(`label[for="${element.getAttribute("id")}"]`).innerText', input_element)
        value = await page.evaluate('(element) => element.value', input_element)
        
        form_data.append({"label": label, "value": value})
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(form_data)
    return df

async def main():
    async with async_playwright() as p:
        # Launch the browser and open a new page
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Navigate to the page with your form
        await page.goto('your_form_url')

        # Extract the form data
        data_frame = await extract_form_data(page, 'form_selector_here')  # Replace 'form_selector_here' with your actual form selector

        # Do something with the data_frame, e.g., print it or save it to a file
        print(data_frame)

        # Close the browser
        await browser.close()

# Run the main function
asyncio.run(main())
