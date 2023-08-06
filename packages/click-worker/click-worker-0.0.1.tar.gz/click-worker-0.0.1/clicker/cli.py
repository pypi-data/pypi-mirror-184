"""
The command-line interface for the clicker
"""
import argparse
from .worker import click

def main():
    parser = argparse.ArgumentParser(
        description="click event woker."
    )
    parser.add_argument(
        "--time","-t", type=int,
        help="clicker time interval."
    )
    args = parser.parse_args()
    click(args.time)

if __name__ == "__main__":
    main()