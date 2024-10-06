from bot.main import web_driver
from config.data import nums

class node:
    def __init__(self,_):
        self.data = self.activate()
        self.left = None
        self.right = None

    def activate(self):
        for i in range(nums.num_nodes):
            func = web_driver()
            func.start_driver()
            func.start_browser()
            func.close_browser()
            


class binary_tree:
    global stack
    global result
    stack = []
    result = []

    def main(self, root:node):
        # in order traversal
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.data)
            root = root.right
            print(f'Node: {node}')
        return result

if __name__ == "__main__":
    try:
        instance = binary_tree()
        root = node(1)
        instance.main(root=root)
    except KeyboardInterrupt:
        print("exiting gracefully...")
        exit(0)
        
