from abc import ABC, abstractmethod
from typing import Tuple, List, TypeVar, Generic
import ast

from base_language_translator import LanguageTranslator


TargetExp = str


def ada_case(name: str) -> str:
    # TODO handle cases where name isn't snake_case
    return name.title()

ASCII_CHARACTERS = {
    "\x00": "ASCII.NUL",
    "\x01": "ASCII.SOH",
    "\x02": "ASCII.STX",
    "\x03": "ASCII.ETX",
    "\x04": "ASCII.EOT",
    "\x05": "ASCII.ENQ",
    "\x06": "ASCII.ACK",
    "\x07": "ASCII.BEL",
    "\x08": "ASCII.BS",
    "\x09": "ASCII.HT",
    "\x0a": "ASCII.LF",
    "\x0b": "ASCII.VT",
    "\x0c": "ASCII.FF",
    "\x0d": "ASCII.CR",
    "\x0e": "ASCII.SO",
    "\x0f": "ASCII.SI",
    "\x10": "ASCII.DLE",
    "\x11": "ASCII.DC1",
    "\x12": "ASCII.DC2",
    "\x13": "ASCII.DC3",
    "\x14": "ASCII.DC4",
    "\x15": "ASCII.NAK",
    "\x16": "ASCII.SYN",
    "\x17": "ASCII.ETB",
    "\x18": "ASCII.CAN",
    "\x19": "ASCII.EM",
    "\x1a": "ASCII.SUB",
    "\x1b": "ASCII.ESC",
    "\x1c": "ASCII.FS",
    "\x1d": "ASCII.GS",
    "\x1e": "ASCII.RS",
    "\x1f": "ASCII.US",
    "\x7f": "ASCII.DEL",
}

def python_string_to_ada_string(s: str) -> str:
    # TODO figure out WTF to do with UTF-8
    s = s.replace('"', '""')
    for c in ASCII_CHARACTERS:
        s.replace(c, f'" & {ASCII_CHARACTERS[c]} & "')
    return s


class TranslationDesignError(Exception):
    pass


class Translator(LanguageTranslator[TargetExp]):

    def __init__(self) -> None:
        super().__init__()
        self.subprogram_name = None

    def gen_literal(self, c: bool | str | int | float | None) -> TargetExp:
        """
        Translate a literal expression
        c: is the literal value
        """
        match c:
            case bool() | int() | float():
                return str(c)
            case str():
                return python_string_to_ada_string(c)
            case None:
                return "null"
            case _:
                raise TranslationDesignError(f"Unhandled expression: {c}")


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
        if self.subprogram_name is None:
            raise TranslationDesignError("subprogram_name should never be None")
        return [f"end {self.subprogram_name};"]

    def no_completion_prompt_stub(self) -> str:
        """
        A default stub to create a syntactically valid translation in case of not performing completion.
        For example, for Rust this could be:

            todo!()
        }
        
        """
        if self.subprogram_name is None:
            raise TranslationDesignError("subprogram_name should never be None")
        return f"end {self.subprogram_name};"


