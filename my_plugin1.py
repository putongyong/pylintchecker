from astroid import nodes
from typing import TYPE_CHECKING, Optional

from pylint.checkers import BaseChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class FunctionNameChecker(BaseChecker):

    name = "too-long-function-name"
    msgs = {
        "W0002": (
            "Function name is too long (more than 20 characters).",
            "too-long-function-name",
            "Function names should be 20 characters or shorter.",
        ),
    }
    options = ()

    def __init__(self, linter: Optional["PyLinter"] = None) -> None:
        super().__init__(linter)
        self._function_stack = []

    def leave_functiondef(self, node: nodes.FunctionDef) -> None:
        self._function_stack.pop()

    def visit_functiondef(self, node: nodes.FunctionDef) -> None:
        self._function_stack.append([])
        
        # Check function name length
        if len(node.name) > 20:
            self.add_message("too-long-function-name", node=node)



def register(linter: "PyLinter") -> None:
    """This required method auto registers the checker during initialization.
    :param linter: The linter to register the checker to.
    """
    linter.register_checker(FunctionNameChecker(linter))
