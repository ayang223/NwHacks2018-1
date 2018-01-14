import argparse
import re

import requests
from bs4 import BeautifulSoup


def main():
    args = parseArgs()


def parseArgs():
    parser = argparse.ArgumentParser("online buy & sell helper")
    parser.add_argument("item", help="ex:beats solo3", type=str)
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()