# FunCLI [![PyPI](https://img.shields.io/pypi/pyversions/funcli.svg?style=plastic)](https://gitlab.com/valtron/funcli)

Automatically generate a simple CLI.

## Installation

```
pip install funcli
```

## Basic Usage

```python
def main(*args: int):
	print("Sum:", sum(args))

if __name__ == '__main__':
	import funcli
	funcli.main()

# $ python sum.py 1 2 3
# Sum: 6
```

## Reference

```python
funcli.main(spec = None)
```

Sugar. `spec` defaults to the `main` function from the caller's scope.
Calls `funcli.run` on `spec`, and calls `sys.exit` with the return value.

```python
funcli.run(spec, args = None, converters = None)
```

- `spec` is either a callable, a sequence of callables, or a dict mapping strings to nested `specs`
- `args` default to `sys.argv[1:]`
- `converters` is a mapping from types (or whatever you want to use as annotations) to a function that parses a command line argument

Given functions `foo`, `bar`, `baz`, here are some sample invocations:

```python
funcli.run(foo, ['arg0']) # Calls foo('arg0')
funcli.run({ foo, bar }, ['bar', 'arg0']) # Calls bar('arg0')
funcli.run({ 'beep': foo, 'bloop': [bar, baz] }, ['beep', 'arg0']) # Calls foo('arg0')
funcli.run({ 'beep': foo, 'bloop': [bar, baz] }, ['bloop', 'bar', 'arg0']) # Calls bar('arg0')
```

### Converters

Built-in converters handle `int`, `float`, `bool`, and `pathlib.Path`. Everything else is kept as a `str`.
