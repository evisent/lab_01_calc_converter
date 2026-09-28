import argparse
import sys

from .calculator import calculation
from .converter import convertation
from .errors import *


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(prog="toolkit", description="Calculator and converter of length, weight and temperature")
    sub = parser.add_subparsers(dest="command", required=True)

    # python -m toolkit calc "EXPRESSION"
    p_calc = sub.add_parser("calc", help="solve the expression")
    p_calc.add_argument("expression")

    # python -m toolkit convert VALUE --from UNIT --to UNIT
    p_conv = sub.add_parser("convert", help="convert unit")
    p_conv.add_argument("value", type=float)
    p_conv.add_argument("--from", dest="from_unit", required=True)
    p_conv.add_argument("--to", dest="to_unit", required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "calc":
            print(calculation(args.expression))
        else:
            print(convertation(args.value, args.from_unit, args.to_unit), args.to_unit)
    except Error as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
