import Extract_Data
import os
import pandas as pd
from tqdm import tqdm
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from urllib.request import urlopen


def create_database(leagues):
    '''
    Scrape the webpage to populate databases that gathers information
    about the standing and the results tables in 2022
    in a specific league
    Parameters
    ----------
    leagues: str or list
        league(s) to extract the data from
    '''
    if type(leagues) is not list:
        leagues = [leagues]
    for league in leagues:
        os.makedirs(f"./Data/Future_Matches/{league}", exist_ok=True)

    list_results = ['Home_Team', 'Away_Team', 'Time',
                    'Link', 'Results', 'Season', 'Round', 'League']
    dict_results = {x: [] for x in list_results}
    ROOT_DIR = "https://www.besoccer.com/competition/scores/"

    for league in leagues:
        URL = ROOT_DIR + league + '/2022'
        try:
            year_url = urlopen(URL)
        except HTTPError as exception:
            if exception.code == 404:
                print('The page does not exist')
            elif exception.code == 302:
                print('The specified year or league does not exist')
            os.remove(f"./Data/Future_Matches/{league}/"
                        + f"Next_Match_{league}.csv")

        year_bs = BeautifulSoup(year_url.read(), 'html.parser')
        num_rounds = Extract_Data.extract_rounds(year_bs)

        URL += "/group1/round" + str(num_rounds+1)
        round_url = urlopen(URL)
        round_bs = BeautifulSoup(round_url.read(), 'html.parser')
        results = Extract_Data.extract_results(round_bs)

        if results is None:
            print(f'-------------------------------------------------')
            print(f'!!!\tRound {num_rounds+1} does not'
                    + f'exist on year 2022\t!!!''')
            print(f'-------------------------------------------------')

        for i, key in enumerate(list_results[:-4]):
            dict_results[key].extend(results[i])

        dict_results['Results'].extend([None] * len(results[0]))
        dict_results['Season'].extend([2022] * len(results[0]))
        dict_results['Round'].extend([num_rounds+1] * len(results[0]))
        dict_results['League'].extend([league] * len(results[0]))

    print(dict_results)
    new_df_results = pd.DataFrame(dict_results)
    new_df_results.to_csv(
            f"./Data/Future_Matches/{league}/"
            + f"Next_Match_{league}.csv",
            mode='w', header=True, index=False)
    for key in dict_results:
        dict_results[key].clear()

if __name__ == '__main__':
    list_leagues = ['2_liga', 'eerste_divisie', 'ligue_2', 'primera_division', 'serie_a', 'bundesliga', 'eredivisie', 'premier_league',
     'segunda_division', 'serie_b', 'championship', 'ligue_1', 'primeira_liga', 'segunda_liga']
    for league in list_leagues:
        create_database(league)