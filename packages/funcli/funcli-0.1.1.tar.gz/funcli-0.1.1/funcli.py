import re
import sys
from collections import defaultdict
from pathlib import Path
import inspect
from typing import List, Optional, Dict, Callable, Any, Tuple, Set

Converter = Callable[[str], Any]
Converters = Dict[object, Converter]
GeneralFunc = Callable[..., Any]
# Recursive types: https://github.com/python/mypy/issues/731
#Spec = Union[GeneralFunc, List[GeneralFunc], Tuple[GeneralFunc], Set[GeneralFunc], Dict[str, 'Spec']]
#Tree = Union[GeneralFunc, Dict[str, 'Tree']]
Spec = Any
Tree = Any

def main(spec: Spec = None) -> None:
	if spec is None:
		spec = inspect.stack()[1][0].f_globals.get('main')
		if spec is None:
			raise KeyError("'main' function not defined")
		if not callable(spec):
			raise TypeError("'main' must be callable")
	sys.exit(run(spec))

def run(spec: Spec, args: Optional[List[str]] = None, *, converters: Optional[Converters] = None) -> Any:
	if args is None:
		args = sys.argv[1:]
	convs = defaultdict(lambda: str, CONVERTERS)
	if converters is not None:
		convs.update(converters)
	tree = spec_to_tree(spec)
	callable, args, kwargs = parse_args(tree, args)
	args, kwargs = convert_args(args, kwargs, callable, convs)
	return callable(*args, **kwargs)

def spec_to_tree(spec: Spec) -> Tree:
	if isinstance(spec, dict):
		return { k: spec_to_tree(v) for k, v in spec.items() }
	if isinstance(spec, (list, set, tuple)):
		return { f.__name__: f for f in spec }
	return spec

def parse_bool(s: str) -> bool:
	if s == 'True': return True
	if s == 'False': return False
	raise ValueError("invalid bool literal: {!r}".format(s))

CONVERTERS: Converters = {
	int: int,
	float: float,
	bool: parse_bool,
	Path: Path,
}

def parse_args(tree: Tree, args: List[str]) -> Tuple[GeneralFunc, List[str], Dict[str, str]]:
	# Iterate over the `select` section of `args` to get `callable`
	i = 0
	while isinstance(tree, dict):
		tree = tree[args[i]]
		i += 1
	callable = tree
	
	args_parsed = []
	kwargs_parsed = {}
	for a in args[i:]:
		m = re.match(r'--([^=]+)=(.*)', a)
		if m:
			kwargs_parsed[m.group(1)] = m.group(2)
		else:
			if kwargs_parsed:
				raise SyntaxError("positional argument follows keyword argument")
			args_parsed.append(a)
	return callable, args_parsed, kwargs_parsed

def convert_args(args: List[str], kwargs: Dict[str, str], f: GeneralFunc, converters: Converters) -> Tuple[List[Any], Dict[str, Any]]:
	argspec = inspect.getfullargspec(f)
	args_converted = []
	kwargs_converted = {}
	for a, sa in zip(args, argspec.args):
		converter = converters[argspec.annotations.get(sa)]
		args_converted.append(converter(a))
	if len(args) > len(argspec.args):
		converter = converters[argspec.annotations.get(argspec.varargs)]
		for i in range(len(argspec.args), len(args)):
			args_converted.append(converter(args[i]))
	annot_varkw = argspec.annotations.get(argspec.varkw)
	for k, a in kwargs.items():
		if k == argspec.varargs:
			raise TypeError("{}() got an unexpected keyword argument {!r}".format(f.__name__, k))
		converter = converters[argspec.annotations.get(k) or annot_varkw]
		kwargs_converted[k] = converter(a)
	return args_converted, kwargs_converted
