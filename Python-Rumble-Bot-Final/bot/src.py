from bot.main import web_driver

class source:
    def activate(self):
        func = web_driver()
        func.start_driver()
        func.start_browser()
        func.quit_driver()
        print(f'node: web_driver activated')