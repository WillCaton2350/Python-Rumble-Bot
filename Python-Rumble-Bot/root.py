from bot.main import web_driver
from config.data import nums

class node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class binary_tree:
    def activate(self):
        func = web_driver()
        func.start_driver()
        func.start_browser()
        func.close_browser()

    def main(self, root:node):
        # in order traversal
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.activate()
            result.append(root.data)
            root = root.right
            print(f'Node: {node}')
        return result

if __name__ == "__main__":
    instance = binary_tree()
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    try:
        for i in range(nums.num_nodes):
            val = instance.main(root)
            print(f'Traversal Pattern: {val}')
            print(f'Execution: {i}')
    except KeyboardInterrupt:
        print("exiting gracefully...")
        exit(0)
