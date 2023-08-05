from .function_call_checker import FunctionCallChecker
from .logic_op_complexity_checker import LogicOpComplexityChecker
from .select_alias_checker import SelectAliasChecker
from .select_cast_checker import SelectCastChecker
from .chained_function_checker import ChainedDotFunctionsSyntaxChecker
from .confluence_page_checker import ConfluencePageChecker
from .author_checker import AuthorChecker
from .case_import_checker import CaseImportChecker
from .module_display_checker import ModuleDisplayChecker

def register(linter):
    linter.register_checker(FunctionCallChecker(linter))
    linter.register_checker(LogicOpComplexityChecker(linter))
    linter.register_checker(SelectAliasChecker(linter))
    linter.register_checker(SelectCastChecker(linter))
    linter.register_checker(ConfluencePageChecker(linter))
    linter.register_checker(ChainedDotFunctionsSyntaxChecker(linter))
    linter.register_checker(AuthorChecker(linter))
    linter.register_checker(CaseImportChecker(linter))
    linter.register_checker(ModuleDisplayChecker(linter))
