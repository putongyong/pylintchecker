import astroid

code = '''
class MyClass:
    l = 42 
    O = 123  
    I = "example"  

    def __init__(self):
        self.x = 'l' 

    def method_with_assignment(self):
        self.O = 1 

'''

# Parse the entire code block
node = astroid.parse(code)

# Get the body of the code (the function definition)
bd = node.body[0]

for i in bd:
    # Check if the statement is an assignment
    if len(i)==1 and i in ('l', 'O', 'I'):
        print(i)