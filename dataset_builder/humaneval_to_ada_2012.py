from abc import ABC, abstractmethod
from typing import Tuple, List, TypeVar, Generic
import ast
import re

from base_language_translator import LanguageTranslator
from humaneval_to_cpp import DOCSTRING_LINESTART_RE

TargetExp = str

ADA_MAIN_NAME = "Main"

ADA_KEYWORDS = {"abort", "abs", "abstract", "accept", "access", "aliased", "all", "and", "array", "at", "begin", "body", "case", "constant", "declare", "delay", "delta", "digits", "do", "else", "elsif", "end", "entry", "exception", "exit", "for", "function", "generic", "goto", "if", "in", "interface", "is", "limited", "loop", "mod", "new", "not", "null", "of", "or", "others", "out", "overriding", "package", "pragma", "private", "procedure", "protected", "raise", "range", "record", "rem", "renames", "requeue", "return", "reverse", "select", "separate", "some", "subtype", "synchronized", "tagged", "task", "terminate", "then", "type", "until", "use", "when", "while", "with", "xor",}

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

CAMEL_REGEX_1 = re.compile('(.)([A-Z][a-z]+)')
CAMEL_REGEX_2 = re.compile('__([A-Z])')
CAMEL_REGEX_3 = re.compile('([a-z0-9])([A-Z])')

def camel_to_snake(name: str) -> str:
    # Taken from: https://stackoverflow.com/a/1176023
    name = CAMEL_REGEX_1.sub(r'\1_\2', name)
    name = CAMEL_REGEX_2.sub(r'_\1', name)
    name = CAMEL_REGEX_3.sub(r'\1_\2', name)
    return name.lower()

def ada_case(name: str) -> str:
    return camel_to_snake(name).title()

def python_string_to_ada_string(s: str) -> str:
    # TODO figure out WTF to do with UTF-8
    s = s.replace('"', '""')
    for c in ASCII_CHARACTERS:
        s.replace(c, f'" & {ASCII_CHARACTERS[c]} & "')
    return s


def coerce(expr: str, type) -> str:
    def coerce_to_option(expr: str) -> str:
        if expr == "None" or expr == "null":
            return "(Valid => False)"
        else:
            return f"(Valid => True, Value => {expr})"
    match expr, type:
        case expr, ast.Subscript(ast.Name("Optional"), _):
            return coerce_to_option(expr)
        case _:
            return expr


class TranslationDesignError(Exception):
    pass


class Translator(LanguageTranslator[TargetExp]):

    def __init__(self) -> None:
        super().__init__()
        self.reinit()
        super().__init__()
        self.string_type = "String"
        self.float_type = "Float"
        self.int_type = "Integer"
        self.bool_type = "Boolean"
        # self.none_type = "Optional.empty()" # TODO figure out None types
        self.array_type = "Array"
        # self.list_type = "ArrayList"  # TODO figure out Vector vs Array, and handling non-fixed length elements e.g. Strings
        # self.tuple_type = "Pair"  # TODO figure out Tuple
        # self.dict_type = "HashMap"  # TODO figure out dict
        # self.optional_type = "Optional"  # TODO figure out. Variant record?
        self.any_type = "Object"  # TODO cry
        self.indent = ' ' * 3
        self._custom_type_decls = []

    def reinit(self) -> None:
        self.subprogram_name = None

    def gen_array_type(self, elem_type):
        element = self.translate_pytype(elem_type)
        type_name = f"{element}_Array"
        decl = f"type {type_name} is array (Integer range <>) of {element};"
        self._custom_type_decls.append(decl)
        return type_name

    def gen_optional_type(self, elem_type):
        element = self.translate_pytype(elem_type)
        type_name = f"{element}_Option"
        decl = f"type {type_name} (Valid : Boolean := False) is record case Valid is when True => Value : {element}; when False => null; end case; end record;"
        self._custom_type_decls.append(decl)
        return type_name

    def translate_pytype(self, ann: ast.expr | None) -> str:
        """Traverses an AST annotation and translate Python type annotation to an Ada Type"""

        if ann == None:
            raise Exception(f"No annotation")

        # Todo add missing Set type
        match ann:
            case ast.Name(id="str"):
                return self.string_type
            case ast.Name(id="int"):
                return self.int_type
            case ast.Name(id="float"):
                return self.float_type
            case ast.Name(id="bool"):
                return self.bool_type
            case ast.Name(id="None"):
                #It appears None is always used in optional
                raise Exception("Not implemented")
            case ast.List(elts=elts):
                raise Exception("Not implemented")
            case ast.Tuple(elts=elts):
                raise Exception("Not implemented")
            case ast.Dict(keys=k,values=v):
                raise Exception("Not implemented")
            case ast.Subscript(value=ast.Name(id="Dict"), slice=ast.Tuple(elts=key_val_type)):
                raise Exception("Dict not implemented")
            case ast.Subscript(value=ast.Name(id="List"), slice=elem_type):
                return self.gen_array_type(elem_type)
            case ast.Subscript(value=ast.Name(id="Tuple"), slice=elts):
                raise Exception("Tuple Not implemented")
            case ast.Subscript(value=ast.Name(id="Optional"), slice=elem_type):
                return self.gen_optional_type(elem_type)
            case ast.Subscript(value=ast.Name(id="Union"), slice=ast.Tuple(elts=elems)):
                raise Exception("Union Not implemented")
            case ast.Name(id="Any"):
                raise Exception("Not implemented")
            case ast.Constant(value=None):
                raise Exception("Not implemented")
            case ast.Constant(value=Ellipsis):
                raise Exception("Translator do not support translating Ellipsis")
            case _other:
                print(f"Unhandled annotation: {ast.dump(ann)}")
                raise Exception(f"Unhandled annotation: {ann}")

    def gen_literal(self, c: bool | str | int | float | None) -> TargetExp:
        """
        Translate a literal expression
        c: is the literal value
        """
        match c:
            case bool() | int() | float():
                return str(c)
            case str():
                return f'"{python_string_to_ada_string(c)}"'
            case None:
                return "null"
            case _:
                raise TranslationDesignError(f"Unhandled expression: {c}")


    def gen_var(self, v: str) -> TargetExp:
        """
        Translate a variable with name v.
        """
        if v in ADA_KEYWORDS:
            return ada_case(f"my_{v}")
        return ada_case(v)

    def gen_list(self, l: List[TargetExp]) -> TargetExp:
        """
        Translate a list with elements l
        """
        match len(l):
            case 0:
                return "(1 .. 0 => <>)"
            case 1:
                return f"(0 => {l[0]})"
            case _:
                return "(" + ", ".join(l) + ")"

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
        return f"{func} ({', '.join(args)})"

    def package_imports(self) -> str:
        # TODO handle cases where more imports are needed e.g. vector/hashmap
        return '\n'.join([
            "pragma Ada_2012;",
        ]) + '\n'

    def translate_prompt(self, name: str, args: List[ast.arg], returns: ast.expr, description: str) -> str:
        """
        Translate Python prompt.
        """
        self.reinit()
        self.type = [[arg.annotation for arg in args], returns]

        main_decl = f"procedure {ADA_MAIN_NAME} is\n\n"
        comment_start = self.indent + '-- '
        ada_description = (
            comment_start + DOCSTRING_LINESTART_RE.sub("\n" + comment_start, description.strip()) + "\n"
        )
        self.subprogram_name = ada_case(name)
        self.subprogram_type = "function"  # TODO figure out when it's a procedure rather than a function
        self.args_type = [self.translate_pytype(arg.annotation) for arg in args]
        formal_args = [f"{self.gen_var(arg.arg)[0]} : {self.translate_pytype(arg.annotation)}" for arg in args]
        formal_arg_list = "; ".join(formal_args)
        self.return_type = self.translate_pytype(returns)
        subprogram_signature = f"{self.subprogram_type} {self.subprogram_name} ({formal_arg_list})"
        self.candidate_signature = f"{self.subprogram_type} Candidate ({formal_arg_list})"
        if self.subprogram_type == "function":
            subprogram_signature = f"{subprogram_signature} return {self.return_type}"
            self.candidate_signature = f"{self.candidate_signature} return {self.return_type}"

        # To be able to use custom types such as arrays of integers, the prompt
        # starts with the specification of a "Placeholder" pacakge where we
        # declare these types. Then comes the declaration the sub-program to be
        # competed, and finally the beginning of "Placeholder" package body.
        #
        # Later in the testsuite prefix/suffix, we add a Main procedure to the
        # output.
        #
        # The result should be an Ada file that contains both the specification
        # and body of a "Placeholder" package, and a main procedure. This will
        # will be split in several .ads and .adb files using gnatchop in
        # evaluation phase.

        ada_spec = f"{self.package_imports()}\n"
        ada_spec += "package Placeholder is\n"
        for typ in list(set(self._custom_type_decls)):
            ada_spec += f"{self.indent}{typ}\n"
        ada_spec += f"{self.indent}{subprogram_signature};\n{ada_description}\n"
        ada_spec += "end Placeholder;\n\n"

        ada_body = f"{self.package_imports()}\n"
        ada_body += "package body Placeholder is\n"
        ada_body += f"{self.indent}{subprogram_signature}"

        ada_prompt = ada_spec + ada_body
        return ada_prompt

    def test_suite_prefix_lines(self, entry_point: str) -> List[str]:
        """
        This code goes at the start of the test suite.
        The entry_point is ???
        """
        return [
                "",
                f"{self.indent}end {self.subprogram_name};",
                "",
                "end Placeholder;",
                "",
                "with Placeholder; use Placeholder;",
                f"procedure Main is",
                f"{self.indent}{self.candidate_signature} renames Placeholder.{self.subprogram_name};",
                "",
                "begin"
            ]

    def test_suite_suffix_lines(self) -> List[str]:
        """
        This code goes at the end of the test suite.
        """
        return [f"end Main;"]

    def deep_equality(self, left: TargetExp, right: TargetExp) -> str:
        """
        All tests are assertions that compare deep equality between left and right.
        """
        return f"{self.indent}pragma Assert ({left} = {right});"

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
        return [f"\n{self.indent}end "]

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

    def finalize(self, result, context) -> str:
        match context:
            case "lhs":
                return result
            case "rhs":
                return coerce(result, self.type[1])
            case _other:
                raise Exception("bad context to finalize")
