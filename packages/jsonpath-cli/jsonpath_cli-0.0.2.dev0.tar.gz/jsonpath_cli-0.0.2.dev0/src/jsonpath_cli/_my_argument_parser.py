import argparse
import json
import numbers
import sys

from jsonpath_tp import get, find
from jsonpath_tp.compile.compile_error import JsonpathSyntaxError
from treepath import MatchNotFoundError, TreepathException


class _MyArgumentParser:
    __slots__ = (
        "parser",
    )

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.__description, epilog=self.__epilog)

        subparsers = self.parser.add_subparsers(help='sub-command help', required=True)

        parser_get = subparsers.add_parser('get', help='gethelp')
        parser_get.set_defaults(func=self.__process_get)
        self.__add_parser_arg_jsonpath(parser_get)
        self.__add_parser_arg_json_file(parser_get)
        self.__add_parser_arg_output(parser_get)

        parser_find = subparsers.add_parser('find', help='gethelp')
        parser_find.set_defaults(func=self.__process_find)
        self.__add_parser_arg_jsonpath(parser_find)
        self.__add_parser_arg_json_file(parser_find)
        self.__add_parser_arg_output(parser_find)

    def process_args(self):
        parsed_args = self.parser.parse_args()

        try:
            parsed_args.output(parsed_args, parsed_args.func)
        except TreepathException as te:
            self.__exit_(1, repr(te))
        except JsonpathSyntaxError as jse:
            self.__exit_(1, jse.pretty_error_message())

    def __exit_(self, status: int, message: str):
        print(message, file=sys.stderr)
        sys.exit(status)

    def __add_parser_arg_jsonpath(self, parser):
        parser.add_argument(
            'jsonpath_expression',
            help="The jsonpath query"
        )

    def __add_parser_arg_json_file(self, parser):
        parser.add_argument(
            'json_files',
            nargs='*',
            help=" '-' for stdin or one or more file paths to json documents",
            type=argparse.FileType('r')
        )

    def __add_parser_arg_output(self, parser):
        output_group = parser.add_argument_group(title="output",
                                                 description="Specify how the output shall be formated")
        group = output_group.add_mutually_exclusive_group()
        group.add_argument("--list", dest="output", action='store_const', const=self.__list_, default=self.__lines)
        group.add_argument("--lines", dest="output", action='store_const', const=self.__lines)
        group.add_argument("--values", dest="output", action='store_const', const=self.__value)

        output_group.add_argument("--indent", type=int, default=None)
        output_group.add_argument("--sort_keys", action='store_true')

    @property
    def __description(self):
        return "Python jsonpath cli utility."

    @property
    def __epilog(self):
        return """
        The jsonpath_cli is a jsonpath implementation built on top of treepath technology.  For details see:
        https://pypi.org/project/jsonpath-tp/
        """

    def __list_(self, parsed_args, process_func):
        my_list = list()
        for result in process_func(parsed_args):
            my_list.append(result)

        print(self.json_dumps(my_list, parsed_args), file=sys.stdout)

    def __lines(self, parsed_args, process_func):
        for result in process_func(parsed_args):
            print(self.json_dumps(result, parsed_args), file=sys.stdout)

    def __value(self, parsed_args, process_func):
        for result in process_func(parsed_args):
            if isinstance(result, str):
                print(result, file=sys.stdout)
            elif isinstance(result, bool):
                print(self.json_dumps(result, parsed_args), file=sys.stdout)
            elif isinstance(result, numbers.Number):
                print(result, file=sys.stdout)
            else:
                print(self.json_dumps(result, parsed_args), file=sys.stdout)

    def __process_get(self, parsed_args):

        last_outer_nf = None

        for json_file in parsed_args.json_files:
            json_data = json.load(json_file)
            try:
                result = get(parsed_args.jsonpath_expression, json_data)
                yield result
                last_outer_nf = None
                break
            except MatchNotFoundError as nf:
                last_outer_nf = nf

        if last_outer_nf is not None:
            raise last_outer_nf

    def __process_find(self, parsed_args):

        last_outer_nf = None

        for json_file in parsed_args.json_files:
            json_data = json.load(json_file)
            try:
                for result in find(parsed_args.jsonpath_expression, json_data):
                    yield result
            except MatchNotFoundError as nf:
                last_outer_nf = nf

        if last_outer_nf is not None:
            raise last_outer_nf

    def json_dumps(self, obj, parsed_args) -> str:
        indent = parsed_args.indent
        sort_keys = parsed_args.sort_keys
        return json.dumps(obj, indent=indent, sort_keys=sort_keys)
