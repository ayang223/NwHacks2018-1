import argparse
import re
import sys


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
    return "https://www.amazon.ca/s/ref=nb_sb_noss_2/133-0145154-2323744?url=search-alias%3Daps&field-keywords=" + searchable_name

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 10

def startChecking(url):
    avg = 0
    max = 0
    min = sys.maxint
    try:
        page = requests.get(url)
        values = []

        soup = BeautifulSoup(page.content, 'html.parser')
        prices = soup.find_all('span', {'class': 's-price'})

        for x in range(0, len(prices)):
            temp = (prices)[x].string.split()
            temp = temp[1].replace("," ,"")
            values.append(float(temp))

        for value in values:
            val = value
            min = val if min > val else min
            max = val if max < val else max
            avg += val

        avg = avg / len(values)
        output = "Highest price : $" + str(max) + "\nLowest price: $" + str(min) + "\nAverage price: $" + str(avg)
        print output

    except Exception as e:
        print("error::", e)



if __name__ == "__main__":
    main()
