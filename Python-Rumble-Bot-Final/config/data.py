from dataclasses import dataclass
from fake_useragent import UserAgent
from time import sleep

@dataclass
class nums:
    node_data: int = 0
    max_retries:int = 3 
    retry_delay: int = 0 
    retries: int = 0
    status: int = 200
    num_executions: int = 100

@dataclass
class urls:
    main_url: str = 'https://rumble.com'

    url_dict = {
    19:'https://rumble.com/v4qi1jf-code-with-me.html',
    20:'https://rumble.com/v4qia7b-code-along.html',
    21:'https://rumble.com/v4ql2ke-coding-a-django-website.html',
    22:'https://rumble.com/v4qlhl8-coding-in-pyqt6-part-1.html',
    23:'https://rumble.com/v4qlkct-coding-in-pyqt6-part-2.html',
    24:'https://rumble.com/v4qluux-coding-a-file-converter.html',
    25:'https://rumble.com/v4qn0ic-coding-a-landing-page-in-django.html',
    26:'https://rumble.com/v4qng8k-coding-a-linked-list-in-selenium.html',
    27:'https://rumble.com/v4qs93b-coding-a-django-website-w-nav-system.html',
    29:'https://rumble.com/v4qsjoi-coding-a-django-website-with-js-designs.html',
    30:'https://rumble.com/v4quetl-coding-a-python-and-django-website-part-1.html',
    31:'https://rumble.com/v4qug3h-coding-a-python-and-django-website-part-2.html',
    32:'https://rumble.com/v4rh0ut-coding-a-test-website-in-django.html',
    33:'https://rumble.com/v4rnsqf-binary-tree-zig-zag-traversal-in-python.html',
    34:'https://rumble.com/v4roau3-binary-tree-in-order-traversal-in-python.html',
    35:'https://rumble.com/v4rv4nf-binary-tree-pre-order-traversal-in-python.html',
    36:'https://rumble.com/v4rx3ll-matrix-spiral-order-traversal-in-python.html',
    37:'https://rumble.com/v4rzwpn-binary-tree-level-order-traversal-in-python.html',
    38:'https://rumble.com/v4s7cct-binary-tree-post-order-traversal-in-python.html',
    39:'https://rumble.com/v4s8bu3-matrix-bfs-shortest-path-in-python.html',
    40:'https://rumble.com/v4ss7e3-two-sum-algo-in-python.html',
    41:'https://rumble.com/v4snlkq-matrix-binary-search-algorithm-in-python.html',
    42:'https://rumble.com/v4sk4e9-generating-a-binary-matrix-in-python.html',
    }

class locators:
    play_btn_xpath: str = '/html/body/main/article/div[2]/div/div[1]/div[1]/div/div/div[1]/div'

class useragents:
    ua = UserAgent()

class time_altered:
    time_buffer = sleep