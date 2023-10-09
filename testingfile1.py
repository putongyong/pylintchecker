import astroid

code = '''
def testing():
    I=4
    l=5
    O=6
    return True
'''

# Parse the entire code block
node = astroid.parse(code)

# Get the body of the code (the function definition)
bd = node.body[0]

# Get the body of the function definition
bdls = bd.body

for i in bdls:
    # Check if the statement is an assignment
    if isinstance(i, astroid.Assign):
        targets = i.targets
        for target in targets:
            # Check if the target is a Name node
            #if isinstance(target, astroid.Name):
            name = target.name
            print(name)
