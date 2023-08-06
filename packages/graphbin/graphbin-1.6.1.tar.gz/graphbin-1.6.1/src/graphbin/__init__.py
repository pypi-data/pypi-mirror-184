#!/usr/bin/env python3

"""graphbin: Refined binning of metagenomic contigs using assembly graphs."""

import os
import sys

from graphbin.utils import (
    graphbin_Canu,
    graphbin_Flye,
    graphbin_MEGAHIT,
    graphbin_Miniasm,
    graphbin_Options,
    graphbin_SGA,
    graphbin_SPAdes,
)


__author__ = "Vijini Mallawaarachchi"
__copyright__ = "Copyright 2019-2022, GraphBin Project"
__credits__ = ["Vijini Mallawaarachchi", "Anuradha Wickramarachchi", "Yu Lin"]
__license__ = "BSD-3"
__version__ = "1.6.1"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "vijini.mallawaarachchi@anu.edu.au"
__status__ = "Production"


def run(args):
    RUNNER = {
        "canu": graphbin_Canu.run,
        "flye": graphbin_Flye.run,
        "megahit": graphbin_MEGAHIT.run,
        "miniasm": graphbin_Miniasm.run,
        "sga": graphbin_SGA.run,
        "spades": graphbin_SPAdes.run,
    }
    RUNNER[args.assembler](args)


def main():
    parser = graphbin_Options.PARSER
    parser.add_argument(
        "--assembler",
        type=str,
        help="name of the assembler used (SPAdes, SGA or MEGAHIT). GraphBin supports Flye, Canu and Miniasm long-read assemblies as well.",
        default="",
    )
    parser.add_argument(
        "--paths",
        default=None,
        required=False,
        help="path to the contigs.paths file, only needed for SPAdes",
    )
    parser.add_argument(
        "--contigs", default=None, help="path to the contigs.fa file.",
    )
    parser.add_argument(
        "--delimiter",
        required=False,
        type=str,
        default=",",
        help="delimiter for input/output results. Supports a comma (,), a semicolon (;), a tab ($'\\t'), a space (\" \") and a pipe (|) [default: , (comma)]",
    )

    args = parser.parse_args()

    if args.version:
        print("GraphBin version %s" % __version__)
        sys.exit(0)

    # Validation of inputs
    # ---------------------------------------------------
    # Check assembler type
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args.assembler = args.assembler.lower()

    if not (
        args.assembler.lower() == "spades"
        or args.assembler.lower() == "sga"
        or args.assembler.lower() == "megahit"
        or args.assembler.lower() == "flye"
        or args.assembler.lower() == "canu"
        or args.assembler.lower() == "miniasm"
    ):
        print(
            "\nPlease make sure to provide the correct assembler type (SPAdes, SGA or MEGAHIT). GraphBin supports Flye, Canu and Miniasm long-read assemblies as well."
        )

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Check assembly graph file
    if not os.path.exists(args.graph):
        print("\nFailed to open the assembly graph file.")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Check if paths files is provided when the assembler type is SPAdes
    if args.assembler.lower() == "spades" and args.paths is None:
        print("\nPlease make sure to provide the path to the contigs.paths file.")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Check contigs.paths file for SPAdes
    if args.assembler.lower() == "spades" and not os.path.exists(args.paths):
        print("\nFailed to open the contigs.paths file.")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Check if contigs.fa files is provided
    if args.contigs is None:
        print("\nPlease make sure to provide the path to the contigs file.")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Check contigs file
    if not os.path.exists(args.contigs):
        print("\nFailed to open the contigs file.")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Check the file with the initial binning output
    if not os.path.exists(args.binned):
        print("\nFailed to open the file with the initial binning output.")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Handle for missing trailing forwardslash in output folder path
    if args.output[-1:] != "/":
        args.output = args.output + "/"

    # Create output folder if it does not exist
    os.makedirs(args.output, exist_ok=True)

    # Validate prefix
    if args.prefix != "":
        if not args.prefix.endswith("_"):
            args.prefix = args.prefix + "_"

    # Validate delimiter
    delimiters = [",", ";", " ", "\t", "|"]

    if args.delimiter not in delimiters:
        print("\nPlease enter a valid delimiter")
        print("Exiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Validate max_iteration
    if args.max_iteration <= 0:
        print("\nPlease enter a valid number for max_iteration")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Validate diff_threshold
    if args.diff_threshold < 0:
        print("\nPlease enter a valid number for diff_threshold")

        print("\nExiting GraphBin...\nBye...!\n")
        sys.exit(1)

    # Remove previous files if they exist
    if os.path.exists(args.output + args.prefix + "graphbin.log"):
        os.remove(args.output + args.prefix + "graphbin.log")
    if os.path.exists(args.output + args.prefix + "graphbin_output.csv"):
        os.remove(args.output + args.prefix + "graphbin_output.csv")
    if os.path.exists(args.output + args.prefix + "graphbin_unbinned.csv"):
        os.remove(args.output + args.prefix + "graphbin_unbinned.csv")

    # Run GraphBin
    # ---------------------------------------------------
    run(args)


if __name__ == "__main__":
    main()
