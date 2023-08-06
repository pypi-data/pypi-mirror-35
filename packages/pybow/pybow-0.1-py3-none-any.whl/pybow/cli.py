#!/usr/bin/env python3
import argparse
import inspect
import pandas as pd
import re
import sys

from collections import namedtuple

from . import props, analysis


def _safe_type_eval(typestr):
    """Returns a type function for a string of its name, for select types.

    Args:
        typestr (str): A str with the name of a type function.
          (str, int, float)

    Returns:
        A type func.
    """
    try:
        return {'str': str, 'int': int, 'float': float,
                'function': _safe_func_eval}[typestr]
    except KeyError:
        return None


def _safe_func_eval(funcstr):
    """Returns a function for a string of its name, for functions in pb.props.

    Args:
        funcstr (str): A str with the name of a function.

    Returns:
        a function.
    """
    return getattr(props, funcstr)


def _make_docstringdict(ds):
    """Parses a google docstring into an Args/Kwargs dict.

    Args:
        ds (str): A google-formatted docstring.

    Returns:
        A dict with Arg/Kwarg name as key, namedtuples with type and help as
        value.
    """
    a = namedtuple('argument', ['type', 'help'])

    # isolate args/kwargs from docstring
    blocks = [block.strip() for block in ds.split('\n\n')]
    args = '\n'.join([block[block.find('\n')+1:]
                     for block in blocks
                     if re.match('(kw)?args:\n', block, flags=re.I)])
    indentdepth = len(args) - len(args.lstrip())
    args_unindent = args.replace(' '*indentdepth, '')

    # split and process separate args into tuples: argname, type, description
    args_split = re.split('\n(?!\s)', args_unindent)
    args_regex = '(\w+)(?: \(([^(]+)\))?: (.+$)'
    args_tuples = [re.match(args_regex, x, flags=re.S).groups()
                   for x in args_split]

    # assemble into a dict
    args_dict = {tup[0]: a(type=_safe_type_eval(tup[1]),
                           help=re.sub('(\s|\n)+', ' ', tup[2]))
                 for tup in args_tuples}

    return args_dict


def _configure_parser(funcs, **parser_kwargs):
    """Configures an argparse.ArgumentParser for a given list of functions.

    Each function’s name becomes a subparser command, each arg a positional
    argument, and each kwarg an optional argument. The called function gets
    stored under the final parser namespace’s func key, as a function object.

    The function’s docstring (google-formatted!) gets parsed and supplies the
    description for each subparser (short description) and argument (entry in
    the args or kwargs block), as well as some basic data type.

    Finally, kwargs with a default of True or False become store_false/true
    optional arguments: A kwarg feature=False becomes an optional argument
    --feature with action='store_true', a kwarg feature=False becomes an
    optional argument --no-feature with action='store_true'.

    The Option -o/--output gets provided to each subparser via a parent parser.

    Args:
        funcs (list): A list of functions to configure the parser for

    Kwargs:
        **parser_kwargs: will get passed to the ArgumentParser.

    Returns:
        An argparse.ArgumentParser.
    """
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-o', '--output',
                               help='Output file. (Default: stdout)',
                               type=argparse.FileType('w'),
                               default=sys.stdout)

    parser = argparse.ArgumentParser(**parser_kwargs)
    subparsers = parser.add_subparsers()

    for func in funcs:
        short_func_desc = func.__doc__[:func.__doc__.find('\n\n')+1]
        p = subparsers.add_parser(func.__name__,
                                  description=short_func_desc,
                                  parents=[parent_parser])
        p.set_defaults(func=func)

        args_dict = _make_docstringdict(func.__doc__)
        signature = inspect.signature(func).parameters
        for arg in signature:
            # empty default: positional arguments
            if signature[arg].default == inspect._empty:
                argname = arg
                parser_kwargs = {'action': 'store',
                                 'type': args_dict[arg].type}
            # else: kwarg -> optional argument
            elif signature[arg].default is True:
                argname = '--no-'+arg
                parser_kwargs = {'action': 'store_false',
                                 'dest': arg}
            elif signature[arg].default is False:
                argname = '--'+arg
                parser_kwargs = {'action': 'store_true'}
            else:
                argname = '--'+arg
                parser_kwargs = {'action': 'store',
                                 'type': args_dict[arg].type}

            p.add_argument(argname,
                           **parser_kwargs,
                           default=signature[arg].default,
                           help=args_dict[arg].help)

    return parser


def pybow_cli():
    """Provides an entry point for the pybow console script."""
    funcs = [analysis.beckhoff1964, analysis.junkmanns2013]

    parser_kwargs = {
        'prog': 'pybow',
        'description': 'Run calculations from the pybow Python library.'
        }
    parser = _configure_parser(funcs, **parser_kwargs)
    args = parser.parse_args()

    args_dict = {k: v
                 for k, v in vars(args).items()
                 if k in inspect.signature(args.func).parameters}

    if len(args_dict) == 0:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        # TODO: find a neater way to handle csv -> DataFrame
        try:
            args_dict['data'] = pd.read_csv(args_dict['data'])
        except KeyError:
            pass

        # TODO: once functions get exposed that break this, local wrapper
        #   functions (returning only the appropriate element from a func call)
        #   can be used.
        results, _ = args.func(**args_dict)

        if args.output == sys.stdout:
            # TODO: make print output look nicer?
            args.output.write(str(results))
        else:
            # TODO: this assumes a pandas object. once functions get exposed
            #   that break this, some type sniffing should be implemented here.
            args.output.write(results.to_json())
    args.output.close()


# quick test for running the cli function without having to install -e pybow
if __name__ == '__main__':
    pybow_cli()
