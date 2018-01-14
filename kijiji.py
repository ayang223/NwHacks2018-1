import argparse
import re

import requests
from bs4 import BeautifulSoup


def main():
    args = parseArgs()
    url = constructURL(args)


def parseArgs():
    parser = argparse.ArgumentParser("online buy & sell helper")
    parser.add_argument("item", help="ex:beats solo3", type=str)
    args = parser.parse_args()

    return args

def constructURL(args):
	print(args)
	try:
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		tables = soup.find_all('tablle', class_='result-title hdrlnk')
		print(tables)
	except Exception as e:
		print('Error: ', e)
		raise

def lookupURL(url):
	try:
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parse')


if __name__ == "__main__":
    main()