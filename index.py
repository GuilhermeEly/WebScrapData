import pandas as pd
import matplotlib.pyplot as plt
import controllers.webScrapperController as wsc
import sqlite3

def main():

    scrapData = wsc.WebScrapperController()
    crypto = 'LRC'
    dataAll, dataCryptoCurrencySub, labelsAll, labelsCryptoCurrencySub = scrapData.getRedditCryptoData(crypto)

    dftodb = pd.DataFrame(zip(labelsAll,dataAll), columns=['DATE','MENTIONS'])
    dftodb['CRYPTO'] = crypto

    print(dftodb)

    # df = pd.DataFrame({'MentionsAllSubs': dataAll, 'MentionsCryptoCurrSub': dataCryptoCurrencySub}, index=labelsAll)
    # print(df)
    
    # df['MA_18'] = df.MentionsAllSubs.rolling(18, min_periods=1).mean() #Média móvel de 180 minutos
    # print(df)
    # df.plot()
    # plt.show()

    conn = sqlite3.connect(r"sqlite\scrap.db")
    #not working properly
    dftodb.to_sql('ScrappedMentionsData', conn, if_exists='append')

main()