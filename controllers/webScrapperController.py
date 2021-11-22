from bs4 import BeautifulSoup
import requests
import re
import datetime as dt

class WebScrapperController:

    def __init__(self):
        pass

    def convertTimestamp(self, timestamp):
        datetimeValues = []
        for ts in timestamp:
            tm = dt.datetime.utcfromtimestamp(ts/1000)
            
            tm = tm - dt.timedelta(minutes=tm.minute % 10,
                             seconds=tm.second,
                             microseconds=tm.microsecond)
        
            datetimeValues.append(tm)

        return datetimeValues

    def getRedditCryptoData(self, crypto):
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

        labelsAll = self.convertTimestamp(labelsAll)
        labelsCryptoCurrencySub = self.convertTimestamp(labelsCryptoCurrencySub)

        return dataAll, dataCryptoCurrencySub, labelsAll, labelsCryptoCurrencySub

    def __del__(self):
        pass