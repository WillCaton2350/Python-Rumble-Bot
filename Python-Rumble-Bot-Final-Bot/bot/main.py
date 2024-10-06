from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from config.data import urls, locators, useragents, time_buffer
from selenium.webdriver.common.by import By
from urllib.error import HTTPError
from seleniumbase import Driver 
import logging

class web_driver:
    def __init__(self):
        self.driver = None
    
    def start_driver(self):
        self.driver = Driver(
        uc=True,incognito=True,
        no_sandbox=True,headless=True)
        user_agent = useragents.ua.random
        self.driver.execute_cdp_cmd(
        f"Network.setUserAgentOverride",
        {"userAgent":user_agent})
        return self.driver

    def start_browser(self):
        for i in urls.url_dict:
            value = urls.url_dict[i]
            try:
                self.driver.get(value)
                WDW(self.driver, 10).until(
                EC.url_to_be(value))
                try:
                    WDW(self.driver,10).until(
                    EC.presence_of_element_located((
                        By.CLASS_NAME,locators.play_btn_classname
                    )))
                    self.driver.find_element(
                    By.CLASS_NAME,locators.play_btn_classname).click()
                    time_buffer.time_altered(1)
                except NoSuchElementException as err:
                    if err:
                        logging.error(f'NoSuchElementException: {err}')
            except WebDriverException as err:
                logging.error(err.msg)
        
        
    def close_browser(self):
        self.driver.quit()
