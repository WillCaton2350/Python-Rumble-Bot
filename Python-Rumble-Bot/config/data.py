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
    main_url: str = 'https://rumble.com'

    url_dict = {
    #1:'https://rumble.com/v4krwyl-traversal.html',
    2:'https://rumble.com/v4krxo9-pandas.html',
    3:'https://rumble.com/v4krxw6-checkers.html',
    4:'https://rumble.com/v4krzqc-ayeagain.html',
    5:'https://rumble.com/v4ks25h-broddin.html',
    6:'https://rumble.com/v4ks44q-frezo.html',
    7:'https://rumble.com/v4ks54r-fact.html',
    8:'https://rumble.com/v4ks5sr-graded.html',
    9:'https://rumble.com/v4ks600-heart-army.html',
    10:'https://rumble.com/v4ks6q9-breathe.html',
    11:'https://rumble.com/v4ks6xk-need4speed.html',
    #12:'https://rumble.com/v4ks7de-oogami.html',
    13: 'https://rumble.com/v4ks8f9-tera.html',
    14: 'https://rumble.com/v4ks8m0-lamn.html',
    15: 'https://rumble.com/v4ks8y9-tintroduction.html',
    #16: 'https://rumble.com/v4ksc0h-twitter-beat.html',
    #17: 'https://rumble.com/v4ksdfr-soubbin.html',
    18:'https://rumble.com/v4kvo2c-ranked.html',
    19: 'https://rumble.com/v4lboxl-regenerate.html'
    }

class locators:
    play_btn_xpath: str = '/html/body/main/article/div[2]/div/div[1]/div[1]/div/div/div[1]/div'

class useragents:
    ua = UserAgent()

class time_altered:
    time_buffer = sleep