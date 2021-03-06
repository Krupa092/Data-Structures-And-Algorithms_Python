#Pre-order traversal using a stack, Tracking State
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 
    def set_value(self,value):
        self.value = value
    def get_value(self):
        return self.value 
    def set_left_child(self,left):
        self.left = left
    def set_right_child(self,right):
        self.right = right
    def get_left_child(self):
        return self.left
    def get_right_child(self):
        return self.right
    def has_left_child(self):
        return self.left != None
    def has_right_child(self):
        return self.right != None 
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"  
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = None
        self.visited_right = None
    def get_node(self):
        return self.node
    def set_visited_left(self,node):
        self.visited_left = True
    def set_visited_right(self,node):
        self.visited_right = True
    def get_visited_left(self):
        return self.visited_left
    def get_visited_right(self):
        return self.visited_right
    def __repr__(self):
        s= f"""{self.node}
        visited_left: {self.visited.left}
        visited_right: {self.visited_right}
        """
def pre_order_with_stack(tree, debug_mode = False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while (node):
        if debug_mode:
            print (f"""
            loop count: {count}
            current node: {node}
            stack: {stack}
            """)
        count +=1
        if node.has_left_child() and not node.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
        elif node.has_right_child() and not node.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.pop()
                node = State.get_node()
            else:
                node = None
    if debug_mode:
        print(f""" loop count: {count}
        current node: {node}
        stack: {Stack}""")
    return visit_order

