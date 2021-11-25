import pandas as pd
import matplotlib.pyplot as plt
import controllers.webScrapperController as wsc
import sqlite3
import time

conn = sqlite3.connect(r"sqlite\scrap.db")

cur = conn.cursor()
query = """SELECT * FROM ScrappedMentionsData"""

cur.execute(query)

#print(cur.fetchone())
data = cur.fetchall()
print(data)
#print(data)

df = pd.DataFrame(data, columns=['DATE', 'MENTIONS', 'CRYPTO']).set_index('DATE')
print(df)

df['MA_18'] = df.MENTIONS.rolling(5, min_periods=1).mean() #Média móvel de 180 minutos
print(df)
df.plot()
plt.show()