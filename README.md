# ⚠️ Python Exception Types

## Built-in Exceptions hierarchy

BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── NameError
      │    └── UnboundLocalError
      ├── AttributeError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── TimeoutError
      ├── RuntimeError
      │    └── RecursionError
      ├── StopIteration
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── MemoryError
      ├── NotImplementedError
      └── SyntaxError
           └── IndentationError

## Descriptions

| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Division or modulo by zero |
| `OverflowError` | Arithmetic result too large to be represented |
| `FloatingPointError` | Floating point operation failed |
| `IndexError` | Sequence index out of range |
| `KeyError` | Dictionary key not found |
| `ValueError` | Correct type but inappropriate value (e.g. `int("abc")`) |
| `TypeError` | Operation applied to wrong type (e.g. `"a" + 1`) |
| `NameError` | Variable or function name not found |
| `UnboundLocalError` | Local variable referenced before assignment |
| `AttributeError` | Object has no such attribute or method |
| `FileNotFoundError` | File or directory does not exist |
| `PermissionError` | Not enough permissions to perform operation |
| `TimeoutError` | Operation timed out |
| `RecursionError` | Maximum recursion depth exceeded |
| `StopIteration` | Iterator has no more items |
| `ModuleNotFoundError` | Imported module not found |
| `MemoryError` | Out of memory |
| `NotImplementedError` | Abstract method not implemented |
| `SyntaxError` | Invalid Python syntax |
| `IndentationError` | Incorrect indentation |
| `SystemExit` | Raised by `sys.exit()` |
| `KeyboardInterrupt` | Program interrupted by user (Ctrl+C) |