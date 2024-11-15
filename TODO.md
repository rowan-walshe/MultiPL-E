# TODO

Stuff to fix :(
mbpp_465_drop_empty

Still to check:
mbpp_237_check_occurences
mbpp_277_dict_filter
mbpp_391_convert_list_dictionary
mbpp_464_check_value


## Already modified

- HumanEval 69 (cleaned-doctests): Removed an extra whitespace that was in one of the doctests
- HumanEval 142 (cleaned-doctests): Fixed the doctests
- MBPP 222 (typed): Fixed typehint. Changed `Any` to `Tuple[Any, ...]`
- MBPP 262 (typed): Fixed typehint. Changed `Any` to `Tuple[List[Any], List[Any]]` to match the docstring and tests
- MBPP 407 (typed): Fixed typehint. Changed `Any` to `Union[int, bool]`.
  - Could be `Union[int, Literal[False]]` to be more accurate, but existing translators won't handle this
- MBPP 413 (typed): Fixed typehint. Changed `List[Any]` to `List[Union[str, int]]`, as the input was restricted to only contain strings and integers.
  - Note that based on the docstring, you could also change the input typehint to take `List[Tuple[Any, ...]]`, and leave the return type as `List[Any]`
- MBPP 446 (typed): Fixed typehint. Changed `Any` to `Tuple[Any, ...]`
- MBPP 587 (typed): Fixed typehint. Changed `Any` to `Tuple[int, ...]`
- MBPP 595 (typed): Fixed typehint. Changed `Any` to `Union[int, Literal['Not Possible']`
  - Note that translators almost certainly don't currently support this typehint. That said, without the typehint, this problem should have been impossible without cheating. How are you supposed to know to return that string rather than None :facepalm:
- MBPP 725 (typed): Fixed typehint. Changed `List[Any]` to `List[str]`
- MBPP 726 (typed): Fixed typehint. Changed `List[Any]` to `List[int]`
- MBPP 744 (typed): Fixed typehint. Changed `Any` to `Tuple[Any, ...]`
- MBPP 754 (typed): Fixed typehint. Changed `List[Any]` to `List[int]`

## Should probably be modified or removed

### MBPP 115
Docstring states it takes a list of dictionaries. Test cases contain both list of dictionaries and dictionary not in a list.

### MBPP 117
Docstring states it takes a list of list. Test cases contain list of tuples

### MBPP 401
Docstring and test cases are list of lists. Function and parameter names indicate they should be tuples of tuples.

### MBPP 417
Function name implies tuples, everything else implies or uses lists

### MBPP 431
Very weird tests that expect the return value to be True or None, not True or False. Typehint could be updated to `Optional[Literal[True]]`, though the existing translators wouldn't support this.

### MBPP 444
Function name implies tuples, everything else implies or uses lists

### MBPP 582
Function name, argument name, and docstring state that the function should check if a dictionary is empty. But two out of 3 test cases use a set, not a dictionary, and the version with typehints specifies that it takes a Set not a Dict.

### MBPP 756
Duplicate of 434. Should it be removed?
