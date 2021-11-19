import pandas as pd
import matplotlib.pyplot as plt
import controllers.webScrapperController as wsc

def main():

    scrapData = wsc.WebScrapperController()
    crypto = 'LRC'
    dataAll, dataCryptoCurrencySub, labelsAll, labelsCryptoCurrencySub = scrapData.getRedditCryptoData(crypto)

    df = pd.DataFrame({'All': dataAll, 'CryptoCurrencySub': dataCryptoCurrencySub}, index=labelsAll)
    df['MA_18'] = df.All.rolling(18, min_periods=1).mean() #Média móvel de 180 minutos
    df.plot()
    plt.show()

main()