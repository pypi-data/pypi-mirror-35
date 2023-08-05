import re
import sys
from collections import defaultdict
from pathlib import Path
import inspect
import argparse
from typing import List, Optional, Dict, Callable, Any, Tuple, Set, get_type_hints

Converter = Callable[[str], Any]
Converters = Dict[object, Converter]
GeneralFunc = Callable[..., Any]
# Recursive types: https://github.com/python/mypy/issues/731
#Spec = Union[GeneralFunc, List[GeneralFunc], Tuple[GeneralFunc], Set[GeneralFunc], Dict[str, 'Spec']]
Spec = Any

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
	parser = argparse.ArgumentParser()
	spec_to_argparse(spec, parser, convs)
	ns = parser.parse_args(args)
	callable = ns._func
	args, kwargs = extract_args(callable, ns)
	return callable(*args, **kwargs)

def spec_to_argparse(spec: Spec, parser: argparse.ArgumentParser, converters: Converters) -> None:
	if isinstance(spec, dict):
		subparsers = parser.add_subparsers()
		for k, v in spec.items():
			spec_to_argparse(v, subparsers.add_parser(k), converters)
		return
	
	if isinstance(spec, (list, set, tuple)):
		subparsers = parser.add_subparsers()
		for f in spec:
			spec_to_argparse(f, subparsers.add_parser(f.__name__), converters)
		return
	
	argspec = inspect.getfullargspec(spec)
	annots = get_type_hints(spec)
	
	parser.set_defaults(_func = spec)
	
	defaults = argspec.defaults or ()
	j = len(argspec.args) - len(defaults)
	for i, arg in enumerate(argspec.args):
		default = (None if i < j else defaults[i - j])
		converter = converters[annots.get(arg)]
		if i < j:
			dest = arg
		else:
			dest = '--' + arg
		if i >= j and annots.get(arg) is bool:
			parser.add_argument(dest, default = default, action = 'store_true')
		else:
			parser.add_argument(dest, default = default, type = converter)
	if argspec.varargs:
		converter = converters[annots.get(argspec.varargs)]
		parser.add_argument(argspec.varargs, type = converter, nargs = '*')
	
	kwonlydefaults = argspec.kwonlydefaults or {}
	for arg in argspec.kwonlyargs:
		converter = converters[annots.get(arg)]
		required = (arg not in kwonlydefaults)
		dest = '--' + arg
		default = kwonlydefaults.get(arg)
		if required or annots.get(arg) is not bool:
			parser.add_argument(dest, default = default, required = required, type = converter)
		else:
			parser.add_argument(dest, default = default, required = required, action = 'store_true')
	if argspec.varkw:
		# TODO
		pass

def extract_args(callable: GeneralFunc, ns: argparse.Namespace) -> Tuple[List[Any], Dict[str, Any]]:
	args = []
	kwargs = {}
	
	argspec = inspect.getfullargspec(callable)
	for arg in argspec.args:
		args.append(getattr(ns, arg))
	if argspec.varargs:
		args.extend(getattr(ns, argspec.varargs))
	for arg in argspec.kwonlyargs:
		kwargs[arg] = getattr(ns, arg)
	if argspec.varkw:
		kwargs.update(getattr(ns, argspec.varkw, {}))
	
	return args, kwargs

def parse_bool(s: str) -> bool:
	if s == 'True': return True
	if s == 'False': return False
	raise ValueError("invalid bool literal: {!r}".format(s))

CONVERTERS = {
	int: int,
	float: float,
	bool: parse_bool,
	Path: Path,
} # type: Converters
