from playwright.sync_api import sync_playwright

class PlaywrightUtil:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

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

if __name__ == '__main__':
    util = PlaywrightUtil()
    util.setup()

    util.open_url('https://example.com')
    util.take_screenshot('example.png')

    util.teardown()
