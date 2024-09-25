from dataclasses import dataclass
from fake_useragent import UserAgent
from time import sleep

@dataclass
class nums:
    num_nodes: int = 100
    node_data: int = 0
    max_retries:int = 3 
    retry_delay: int = 0 
    retries: int = 0
    status: int = 200
    num_executions: int = 10

@dataclass
class urls:
    main_url: str = 'https://www.example.com'

    url_dict = {
    1:'https:/www.example.com',
    }

class locators:
    play_btn_xpath: str = '/html/body/main/article/div[2]/div/div[1]/div[1]/div/div/div[1]/div'

class useragents:
    ua = UserAgent()

class time_altered:
    time_buffer = sleep