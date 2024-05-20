from dataclasses import dataclass
from fake_useragent import UserAgent
from time import sleep

@dataclass(frozen=True)
class nums:
    node_data: int = 0
    max_retries:int = 3 
    retry_delay: int = 0 
    retries: int = 0
    status: int = 200
    counter: int = 0
    num_nodes: int = 100

@dataclass
class urls:
    url_dict = {
    1:'https://www.example_1.com',
    2:'https://www.example_2.com',
    3:'https://www.example_3.com',
    4:'https://www.example_4.com',
    }

class locators:
    play_btn_xpath: str = '/html/body/main/article/div[2]/div/div[1]/div[1]/div/div/div[1]/div'

class useragents:
    ua = UserAgent()

class time_altered:
    time_buffer = sleep
