import pandas as pd
import matplotlib.pyplot as plt
import controllers.webScrapperController as wsc
import sqlite3
import time

def main():
    while True:
        scrapData = wsc.WebScrapperController()
        crypto = 'LRC'
        dataAll, dataCryptoCurrencySub, labelsAll, labelsCryptoCurrencySub = scrapData.getRedditCryptoData(crypto)

        dftodb = pd.DataFrame(zip(labelsAll,dataAll), columns=['DATE','MENTIONS'])
        dftodb['CRYPTO'] = crypto
        dftodb = dftodb.iloc[-5:]
        print(dftodb)

        # df = pd.DataFrame({'MentionsAllSubs': dataAll, 'MentionsCryptoCurrSub': dataCryptoCurrencySub}, index=labelsAll)
        # print(df)

        # df['MA_18'] = df.MentionsAllSubs.rolling(18, min_periods=1).mean() #Média móvel de 180 minutos
        # print(df)
        # df.plot()
        # plt.show()

        conn = sqlite3.connect(r"sqlite\scrap.db")
        #to_sql always drops the table if it exists
        dftodb.to_sql('ScrappedMentionsData', conn, if_exists='replace', index=False)
        time.sleep(180)

main()