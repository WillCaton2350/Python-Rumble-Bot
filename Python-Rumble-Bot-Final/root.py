from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from urllib.error import HTTPError
from seleniumbase import Driver
from random import randint
from config.data import *
import logging

class web_driver:
    def __init__(self):
        self.driver = None
    
    def start_driver(self):
        self.driver = Driver(uc=True)
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
                            logging.error(err)
                            nums.retries += 1
                    break 
                except HTTPError as err:
                    if err.code != nums.status:
                        logging.error(err)
                        nums.retries += 1
                        

    def quit_driver(self):
        self.driver.close()


if __name__ == "__main__":
    for i in range(nums.num_executions):
        func = web_driver()
        func.start_driver()
        func.start_browser() 
        func.quit_driver()
        print(f'node: web_driver activated')

