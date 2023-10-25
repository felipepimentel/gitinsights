with QuickSightAutomation() as util:
    util.login_quick_sight("https://sua_url_inicial.com", "sua_conta", "seu_usuario", "sua_senha")


class QuickSightAutomation(PlaywrightUtil):
    
    def login_quick_sight(self, initial_url, account, username, password):
        # Navegar para a URL inicial
        self.open_url(initial_url)
        
        # Aguardar o redirecionamento e o carregamento da página da conta
        self.page.wait_for_selector("input[name='account']")

        # Preencher e enviar a conta
        self.type_text("input[name='account']", account)
        self.click_selector("button[type='submit']")
        
        # Aguardar o redirecionamento e o carregamento da página de login
        self.page.wait_for_selector("input[name='username']")
        
        # Preencher usuário e senha
        self.type_text("input[name='username']", username)
        self.type_text("input[name='password']", password)
        
        # Clicar no botão de login
        self.click_selector("button[type='submit']")
        
        # Aguardar pelo redirecionamento para a página inicial do QuickSight ou para outro elemento específico
        self.page.wait_for_selector("seu_seletor_especifico")


from playwright.sync_api import sync_playwright

class PlaywrightUtil:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.teardown()

    def setup(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()

    def teardown(self):
        self.browser.close()
        self.playwright.stop()

    def open_url(self, url):
        self.page.goto(url)

    def click_selector(self, selector):
        self.page.click(selector)

    def type_text(self, selector, text):
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.inner_text(selector)

    def take_screenshot(self, path):
        self.page.screenshot(path=path)

# Uso
with PlaywrightUtil() as util:
    util.open_url('https://example.com')
    util.take_screenshot('example.png')
