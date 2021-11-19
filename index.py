from bs4 import BeautifulSoup
import requests
import re
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

def convertTimestamp(timestamp):
    datetimeValues = []
    for ts in timestamp:
        datetimeValues.append(dt.datetime.utcfromtimestamp(ts/1000))

    return datetimeValues

def getRedditCryptoData(crypto):
    url = 'https://apewisdom.io/cryptocurrencies/'+crypto+'/'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    #Get the data thar is how many people are talking about the crypto
    itemData = soup.find("script", text=re.compile(r'\bdata:\s*\['))

    matchData = re.findall(r'\bdata:\s*\[([^][]*)]', itemData.string)

    if matchData:
        dataAll = map(int, matchData[0].split(','))
        dataCryptoCurrencySub = map(int, matchData[1].split(','))

    #Get the labels, which are the datetime
    itemLabels = soup.find("script", text=re.compile(r'\blabels:\s*\['))

    matchLabels = re.findall(r'\blabels:\s*\[([^][]*)]', itemLabels.string)

    if matchLabels:
        labelsAll = map(int, matchLabels[0].split(','))
        labelsCryptoCurrencySub = map(int, matchLabels[1].split(','))

    labelsAll = convertTimestamp(labelsAll)
    labelsCryptoCurrencySub = convertTimestamp(labelsCryptoCurrencySub)

    return dataAll, dataCryptoCurrencySub, labelsAll, labelsCryptoCurrencySub

def main():
    crypto = 'LRC'
    dataAll, dataCryptoCurrencySub, labelsAll, labelsCryptoCurrencySub = getRedditCryptoData(crypto)

    df = pd.DataFrame({'All': dataAll, 'CryptoCurrencySub': dataCryptoCurrencySub}, index=labelsAll)
    df.plot()
    plt.show()

main()