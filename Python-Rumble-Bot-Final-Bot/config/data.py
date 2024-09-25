from dataclasses import dataclass
from fake_useragent import UserAgent
from time import sleep

@dataclass
class nums:
    num_nodes: int = 10

class time_buffer:
    time_altered = sleep

class urls:
    url_dict = {
    1:'www.example.com/',
    2:'',
    }

class locators:
    play_btn_classname: str = 'bigPlayUIInner'
   

class useragents:
    ua = UserAgent()