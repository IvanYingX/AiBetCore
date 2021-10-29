import pandas as pd
from numpy import NAN
import requests
from bs4 import BeautifulSoup
import lxml

df = pd.read_csv('./results_elo.csv') # 146496

df['Elo_away'] = df['Elo_away'].replace(1,NAN)


df_0 = df[df['Elo_home']==0]
links = df_0['Link']

# df.insert(12,'Elo_home', 0)
# df.insert(13,'Elo_away', 0)

for i in df_0.index: # TOFIX: not a range but index as a list? 
    r = requests.get(f'{links[i]}/analysis')
    soup = BeautifulSoup(r.content, 'lxml')
    elo_ele = soup.find(attrs={'id':'match'}).find_all(attrs={"class":"rating"})
    try:
        home_elo = elo_ele[0].text
        away_elo = elo_ele[1].text
    except:
        home_elo = 1
        away_elo = 1
    #updates dataframe
    print(home_elo)
    df_0.loc[i,'Elo_home'] = home_elo
    df_0.loc[i,'Elo_away'] = away_elo

df.update(df_0) #use merge
df.to_csv('./results_wELO.csv', index=False)