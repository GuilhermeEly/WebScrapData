import pandas as pd
import matplotlib.pyplot as plt
import controllers.webScrapperController as wsc
import sqlite3
import time

def main():
    scrapData = wsc.WebScrapperController()

    while True:
        crypto = 'LRC'
        dftodb = scrapData.getRedditCryptoData(crypto)
        print(dftodb)

        # df = pd.DataFrame({'MentionsAllSubs': dataAll, 'MentionsCryptoCurrSub': dataCryptoCurrencySub}, index=labelsAll)
        # print(df)

        # df['MA_18'] = df.MentionsAllSubs.rolling(18, min_periods=1).mean() #Média móvel de 180 minutos
        # print(df)
        # df.plot()
        # plt.show()

        conn = sqlite3.connect(r"sqlite\scrap.db")

        cur = conn.cursor()

        query = """INSERT OR REPLACE INTO ScrappedMentionsData (DATE, CRYPTO, MENTIONS) 
                VALUES ((?), (?), (?))"""

        for i in range(len(dftodb)):
            cur.execute(query, (str(dftodb.DATE[i]), str(dftodb.CRYPTO[i]), str(dftodb.MENTIONS[i]),))
            conn.commit()
        time.sleep(180)

main()