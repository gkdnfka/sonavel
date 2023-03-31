import os
import pandas as pd

from bs4 import BeautifulSoup as bs

import requests
import time
import config


df = pd.read_csv(os.path.join(config.ROOT_DIR, 'data', 'week17.csv'))

if not os.path.isfile(os.path.join(config.ROOT_DIR, 'result', 'result.csv')):
    result = pd.DataFrame(columns=['user1_name', 'user1_class', 'user1_level',
                                   'user2_name', 'user2_class', 'user2_level',
                                   'user3_name', 'user3_class', 'user3_level',
                                   'user4_name', 'user4_class', 'user4_level',
                                   'cleartime'])
else:
    result = pd.read_csv(os.path.join(config.ROOT_DIR, 'result', 'result.csv'))
page_path = 'https://lostark.game.onstove.com/Profile/Character/'

print(result)
for idx in df.index:
    col = {}
    for i in range(1, 5):
        #driver.get(page_path + df.at[idx, f'user{i}_name'])
        response = requests.get(page_path + df.at[idx, f'user{i}_name'])
        soup = bs(response.text, "html.parser")
        try:
            col[f'user{i}_name'] = df.at[idx, f'user{i}_name']
            col[f'user{i}_class'] = config.CLASS_CODE[
                soup.find('img', {'class': 'profile-character-info__img'}).get('alt')]
            col[f'user{i}_level'] = '.'.join(
                soup.find('div', {'class':'level-info2__item'}).text.split('.')[-2:])

        except AttributeError:
            print(df.at[idx, f'user{i}_name'])
            continue

        time.sleep(3)
    col['cleartime'] = df.at[idx, 'cleartime']
    print(col)
    result = result.append(col, ignore_index=True)
    print(f'{idx} party input success')

result.to_csv(os.path.join(config.ROOT_DIR, 'result', 'result.csv'), encoding='utf-8-sig', index=False)




