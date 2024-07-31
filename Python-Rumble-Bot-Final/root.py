from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from undetected_chromedriver.options import ChromeOptions
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from urllib.error import HTTPError
from random import randint
from config.data import *
import logging
import ssl

class web_driver:
    def __init__(self):
        self.driver = None
    
    def start_driver(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        options = ChromeOptions()
        options.add_argument("--single-process")
        options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-cache")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--mute-audio")
        self.driver = uc.Chrome(options=options)
        user_agent = useragents.ua.random
        self.driver.execute_cdp_cmd(
        f"Network.setUserAgentOverride",
        {"userAgent":user_agent})
        return self.driver
    
    def start_browser(self):
        for i in urls.url_dict:
            value = urls.url_dict[i]
            while nums.retries < nums.max_retries:
                try:
                    self.driver.get(value)
                    WDW(self.driver, 10).until(EC.url_to_be(value))
                    try:
                        WDW(self.driver,10).until(
                        EC.presence_of_element_located((
                            By.XPATH,locators.play_btn_xpath
                        )))
                        self.driver.find_element(
                            By.XPATH,locators.play_btn_xpath).click()
                        time_altered.time_buffer(2)
                    except NoSuchElementException as err:
                        if err:
                            logging.error(f'NoSuchElementException: {err}')
                            logging.info(f"Retrying Element in {nums.retry_delay} seconds...")
                            nums.retry_delay = self.fibonacci(nums.retry_delay)
                            nums.retries += 1
                    break 
                except HTTPError as err:
                    if err.code != nums.status:
                        logging.error(f"HTTP error occurred: {err}")
                        logging.info(f"Retrying in {nums.retry_delay} seconds...")
                        nums.retry_delay = self.fibonacci(nums.retry_delay)
                        nums.retries += 1
    @staticmethod
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            sequence = [0, 1]
            for i in range(2, n):
                random_increment = randint(1, 5)
                next_number = sequence[-1] + sequence[-2] + random_increment
                sequence.append(next_number)
            return sequence
    n = 10  
    fibonacci_sequence = fibonacci(n)

    def quit_driver(self):
        self.driver.close()


if __name__ == "__main__":
    for i in range(nums.num_executions):
        func = web_driver()
        func.start_driver()
        func.start_browser()
        func.quit_driver()
        print(f'node: web_driver activated')

