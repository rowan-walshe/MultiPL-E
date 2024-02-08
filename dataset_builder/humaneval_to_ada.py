from abc import ABC, abstractmethod
from typing import Tuple, List, TypeVar, Generic
import ast

from base_language_translator import LanguageTranslator


TargetExp = str


def ada_case(name: str) -> str:
    # TODO handle cases where name isn't snake_case
    return name.title()



class Translator(LanguageTranslator[TargetExp]):
    def gen_literal(self, c: bool | str | int | float | None) -> TargetExp:
        """
        Translate a literal expression
        c: is the literal value
        """
        return "TODO"

    def gen_var(self, v: str) -> TargetExp:
        """
        Translate a variable with name v.
        """
        return "TODO"

    def gen_list(self, l: List[TargetExp]) -> TargetExp:
        """
        Translate a list with elements l
        """
        return "TODO"

    def gen_tuple(self, t: List[TargetExp]) -> TargetExp:
        """
        Translate a tuple with elements t
        """
        return "TODO"

    def gen_dict(self, keys: List[TargetExp], values: List[TargetExp]) -> TargetExp:
        """
        Translate a dictionary with keys and values
        """
        return "TODO"

    def gen_call(self, func: TargetExp, args: List[TargetExp]) -> TargetExp:
        """
        Translate a function call `func(args)`
        """
        return "TODO"

    def translate_prompt(self, name: str, args: List[ast.arg], returns: ast.expr, description: str) -> str:
        """
        Translate Python prompt.
        """
        self.subprogram_name = ada_case(name)
        return f"function {self.subprogram_name}"

    def test_suite_prefix_lines(self, entry_point: str) -> List[str]:
        """
        This code goes at the start of the test suite.
        The entry_point is ???
        """
        return ["begin", "   "]

    def test_suite_suffix_lines(self) -> List[str]:
        """
        This code goes at the end of the test suite.
        """
        return ["end Test;", ""]

    def deep_equality(self, left: TargetExp, right: TargetExp) -> str:
        """
        All tests are assertions that compare deep equality between left and right.
        """
        return "TODO"

    def file_ext(self) -> str:
        """
        The file extension for this language
        """
        return "adb"

    def stop(self) -> List[str]:
        """
        The list of stop tokens for this language
        """
        return [f"end {self.subprogram_name};"]

    def no_completion_prompt_stub(self) -> str:
        """
        A default stub to create a syntactically valid translation in case of not performing completion.
        For example, for Rust this could be:

            todo!()
        }
        
        """
        return f"end {self.subprogram_name};"


