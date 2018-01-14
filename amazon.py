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

def constructUrl(args):
    item_name = args.item
    temp_name = item_name.split(str="", 1)
    searchable_name = "";
    for word in temp_name:
        searchable_name += word + "+"
    searchable_name = searchable_name[:-1]
    return "https://www.amazon.ca/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + searchable_name"

if __name__ == "__main__":
    main()
