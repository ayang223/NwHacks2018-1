import argparse
import re
import sys
import string


import requests
from bs4 import BeautifulSoup


def main():
    print 'abc'
    args = parseArgs()
    url = constructUrl(args)
    processOutputCraigslist(getRawData(url), args)


def parseArgs():
    parser = argparse.ArgumentParser("online buy & sell helper")
    parser.add_argument("item", help="ex:beats solo3", type=str)
    args = parser.parse_args()

    return args


def constructUrl(args):
    value = str(args.item)
    value =  string.replace(value, ' ', '%20')
    value += '&sort=rel'
    url = 'https://vancouver.craigslist.ca/search/sss?query=' + value

    return url


def getRawData(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
# <<<<<<< claidev

#         tables = soup.find_all('table', class_='result-title hdrlnk')
#         print(tables)
#     except Exception as e:
#         print('Error: ', e)
#         raise
# =======
        amounts = soup.find_all('span', {'class':'result-price'})

        return amounts
    except Exception as e:
        print(e)
        raise


def processOutputCraigslist(amounts, args):
    prices = []
    avg = 0
    max = 0
    min = sys.maxint
# >>>>>>> master

    for amount in amounts:
        val = int(amount.string[1:])
        if(val != 1):
            min = val if min > val else min
            max = val if max < val else max
            avg += val

# <<<<<<< claidev
# def lookupURL(url):
#     try:
#         page = requests.get(url)
#         print page
#         print 'aaa'
#         soup = BeautifulSoup(page.content, 'html.parser')

#         tables = soup.find_all('div', {'id':'sortable-results'})
#         print tables
# =======
    avg = avg / len(amounts)
    output = "Price of "+ str(args.item) +" has " + "average price value = $" + str(avg) + ", min price value = $" + str(min) + ", and max price value = $" + str(max) + " on Craigslist";

    print output
# >>>>>>> master

    except Exception as e:
        print(e)
        raise

if __name__ == "__main__":
    main()
