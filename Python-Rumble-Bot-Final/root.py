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
    
    root.left.left.left = node(8)
    root.left.left.right = node(9)
    root.left.right.left = node(10)
    root.left.right.right = node(11)
    
    root.right.left.left = node(12)
    root.right.left.right = node(13)
    root.right.right.left = node(14)
    root.right.right.right = node(15)

    root.left.left.left.left = node(16)
    root.left.left.left.right = node(17)
    root.left.left.right.left = node(18)
    root.left.left.right.right = node(19)

    root.left.right.left.left = node(20)
    root.left.right.left.right = node(21)
    root.left.right.right.left = node(22)
    root.left.right.right.right = node(23)

    root.right.left.left.left = node(24)
    root.right.left.left.right = node(25)
    root.right.left.right.left = node(26)
    root.right.left.right.right = node(27)
    
    root.right.right.left.left = node(28)
    root.right.right.left.right = node(29)
    root.right.right.right.left = node(30)
    root.right.right.right.right = node(31)

    try:
        for i in range(nums.num_executions):
            val = instance.main(root)
            print(f'Traversal Pattern: {val}')
            print(f'Execution: {i}')
    except KeyboardInterrupt:
        print("exiting gracefully...")
        exit(0)
