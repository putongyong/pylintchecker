import astroid

code = '''
I=4
l=5
O=6
'''

# Parse the entire code block
node = astroid.parse(code)
#tree=node.repr_tree()
#print(tree)
bd=node.body
for i in bd:
    targets=i.targets
    for target in targets:
        print(target.name)