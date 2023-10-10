from astroid import nodes
from typing import TYPE_CHECKING, Optional

from pylint.checkers import BaseChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter

class NamesToAvoidChecker(BaseChecker):
    name = "names-to-avoid"
    msgs = {
        "W0002": (
            "Never use the characters ‘l’, ‘O’, or ‘I’ as single character variable names.",
            "names-to-avoid",
            "In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use ‘l’, use ‘L’ instead.",
        ),
    }
    options = ()
    
    def __init__(self, linter: Optional["PyLinter"] = None) -> None:
        super().__init__(linter)
        self._function_stack = []
    
    def visit_assign(self, node: nodes.Assign) -> None:
        if not isinstance(node,nodes.Assign):
            return
        for target in node.targets:
            try:
                name = target.name
            except:
                name = target.attrname
            if name and len(name) == 1 and name in ('l', 'O', 'I'):
                self.add_message("names-to-avoid", node=node)
    
    def visit_classdef(self, node: nodes.Module) -> None:
        '''
        try:
            bd = node.body
            if isinstance(bd,nodes.Assign):
                targets = bd.targets
                for target in targets:
                    name = target.name
                    if name and len(name) == 1 and name in ('l', 'O', 'I'):
                        self.add_message("names-to-avoid", node=node)
        except:
            bd = node.body[0].body[0].body
            if isinstance(bd,nodes.Assign):
                name = bd[0].targets[0].attrname
                if name and len(name) == 1 and name in ('l', 'O', 'I'):
                    self.add_message("names-to-avoid", node=node)
        '''
        if node.body:
            bd = node.body
            if isinstance(bd,nodes.Assign):
                targets = bd.targets
                for target in targets:
                    name = target.name
                    if name and len(name) == 1 and name in ('l', 'O', 'I'):
                        self.add_message("names-to-avoid", node=node)

    def visit_functiondef(self, node: nodes.FunctionDef) -> None:
        
        self._function_stack.append([])
        
        if isinstance(node,nodes.FunctionDef):
        
            bd = node.body[0]
            if isinstance(bd,nodes.Assign):
                targets = bd.targets
                for target in targets:
                    try:
                        name = target.name
                    except:
                        name = target.attrname
                    if name and len(name) == 1 and name in ('l', 'O', 'I'):
                        self.add_message("names-to-avoid", node=node)
    
    def leave_functiondef(self, node: nodes.FunctionDef) -> None:
        self._function_stack.pop()

    

def register(linter: "PyLinter") -> None:
    linter.register_checker(NamesToAvoidChecker(linter))
