from bot.main import web_driver
from config.data import *

class node:
    def __init__(self,_):
        self.data = self.activate()
        self.left = None
        self.right = None 

    def activate(self):
        for i in range(nums.num_executions):
            func = web_driver()
            func.start_driver()
            func.start_browser()
            func.quit_driver()
            print(f'node:{node} {i}')

class binary_tree:
    def main(self,root:node):
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.data)
            root = root.right
        return result
            
if __name__ == "__main__":
    try:
        instance = binary_tree()
        root = node(1)
        root.left = node(2)
        root.right = node(3)
        instance.main(root=root)
    except KeyboardInterrupt:
        print(' exiting gracefully...')
        exit(0)
