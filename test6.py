# Top-level variables
l = 1
O = 'hello'
I = 3.14

def test_function():
    # Variables within a function
    l = 'local_l'
    O = 42
    I = [1, 2, 3]

    class TestClass:
        # Variables within a class
        l = 'class_l'
        O = 3.0
        I = (4, 5, 6)

        def __init__(self):
            # Variables within a class method
            self.l = 'method_l'
            self.O = True
            self.I = {'key': 'value'}

    # Function body
    local_l = 123
    local_O = 'world'
    local_I = 2.71

test_instance = test_function()
