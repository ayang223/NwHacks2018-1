import argparse
import re

import requests
from bs4 import BeautifulSoup

from time import sleep

def main():
    args = parseArgs()
    url = constructUrl(args)
    startChecking(url)

def parseArgs():
    parser = argparse.ArgumentParser("online buy & sell helper")
    parser.add_argument("item", help="ex:beats solo3", type=str)
    args = parser.parse_args()

    return args

def constructUrl(args):

    item_name = args.item
    temp_name = item_name.split()
    searchable_name = "";
    for word in temp_name:
        searchable_name += word + "+"
    searchable_name = searchable_name[:-1]
    # return "https://www.facebook.com/marketplace/search?query=" + searchable_name
    return "https://www.amazon.ca/s/ref=nb_sb_noss_2/133-0145154-2323744?url=search-alias%3Daps&field-keywords=" + searchable_name

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 10

def startChecking(url):
    print("checking")
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # soup = BeautifulSoup(page.page_source, 'lxml')
        prices = soup.find_all('span', {'class': 's-price'})
        print len(prices)
        for x in range(0, len(prices)):
            print (prices)[x].string
    except Exception as e:
        print("error::", e)



if __name__ == "__main__":
    main()
