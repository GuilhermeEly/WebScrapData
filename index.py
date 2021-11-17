from bs4 import BeautifulSoup
import requests
import ast  # abstract syntax tree to parse dictionary text
import json
import re

url = 'https://apewisdom.io/cryptocurrencies/LRC/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

#700 -> 419
#547 -> 268
#153

#label1 -> 582
#data1  -> 584

#label2 -> 640
#data2  -> 642

# line_number = 642

# li = soup.prettify().split('\n')
# print (str(li[line_number-1]))

# labe1 = str(li[line_number-1]).split(',')
# print(labe1)

# Get the script node with text matching your pattern
item = soup.find("script", text=re.compile(r'\blabels:\s*\['))
#print(item)
match = re.search(r'\blabels:\s*\[([^][]*)]', item.string)
#print(match[1])
if match:
    labels = map(int, match.group(1).split(','))

print(list(labels))

item2 = soup.find("script", text=re.compile(r'\bdata:\s*\['))
#print(item2)
match2 = re.search(r'\bdata:\s*\[([^][]*)]', item2.string)
#print(match2.group(1))
#print(match2.group(2))
if match2:
    labels2 = map(int, match2.group(1).split(','))

print(list(labels2))