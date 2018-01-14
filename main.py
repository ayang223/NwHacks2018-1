import argparse
import re


import requests
from bs4 import BeautifulSoup


def main():
    args = parseArgs()
    #url = contructUrl(args)
    url = 'https://vancouver.craigslist.ca/search/sss?query=beats%20solo%203&sort=rel'
    lookupURL(url)


def parseArgs():
    parser = argparse.ArgumentParser("online buy & sell helper")
    parser.add_argument("item", help="ex:beats solo3", type=str)
    args = parser.parse_args()

    return args


def constructUrl(args):
    try:
        page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		tables = soup.find_all('table', class_='result-title hdrlnk')
		print(tables)
	except Exception as e:
		print('Error: ', e)
		raise


def lookupURL(url):
	try:
		page = requests.get(url)
		soup = BeautifulSoul(page.content, 'html.parser')

		tables = soup.find_all('rows', {'id':'sortable-results'})
		print(tables)


if __name__ == "__main__":
    main()
