import argparse
import re
import sys
reload(sys);
sys.setdefaultencoding("utf8")
import string


import requests
from bs4 import BeautifulSoup
from decimal import *
from math import *


def main():
    args = parseArgs()
    url = constructkijijiURL(args)
    #url = 'https://www.kijiji.ca/b-buy-sell/greater-vancouver-area/beats-solo3/k0c10l80003'
    proccessOutputKijiji(lookupURL(url), args)




def parseArgs():
    parser = argparse.ArgumentParser("online buy & sell helper")
    parser.add_argument("item", help="ex:beats solo3", type=str)
    args = parser.parse_args()

    return args


def constructkijijiURL(args):
	value = str(args.item)
	value = string.replace(value, ' ', '-')
	value += '/k0c10l80003'
	url = 'https://www.kijiji.ca/b-buy-sell/greater-vancouver-area/' + value

	return url

def lookupURL(url):

    try:
    	page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        tables = soup.find_all('div', {'class':'price'})
        return tables

    except Exception as e:
        print(e)
        raise

def proccessOutputKijiji(values,args):
	prices = []
	avg = 0
	max = 0
	min = sys.maxint

	for value in values:
		value = string.replace(str(value.string), ',','')
		val = value.strip()
		#print val
		if val.find('$') != -1:
			price = int(floor(float(val[1:])))
			min = price if min > price else min
			max = price if max < price else max
			avg += price

	avg = avg/len(values)
	output = "Price of "+ str(args.item)+" has "+"average price value = $" + str(avg) + ", min price value = $"+str(min) + ",max price value = $" + str(max) +" on Kijiji";

	print output



if __name__ == "__main__":
    main()
