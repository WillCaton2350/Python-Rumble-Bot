from fake_useragent import UserAgent
from dataclasses import dataclass
from time import sleep

@dataclass(frozen=True)
class nums:
    max_retries:int = 3 
    retry_delay: int = 0 
    retries: int = 0
    status: int = 200
    counter: int = 0
    num_executions: int = 10000

@dataclass(frozen=True)
class urls:
    url_dict = {
    1:'',
    2:'',
    3:'',
    }

class locators:
    play_btn_xpath: str = '/html/body/main/article/div[2]/div/div[1]/div[1]/div/div/div[1]/div'

class useragents:
    ua = UserAgent()

class time_altered:
    time_buffer = sleep
