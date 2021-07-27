import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://basketball.realgm.com/nba/stats/2021/Averages/Qualified/points/All/desc/1/Regular_Season'

# table-989

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'tablesaw', 'data-tablesaw-mode': 'swipe'})

trs = table.find_all('tr')

rows = []
columns = ['#','Player','Team','GP','MPG','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','TOV','PF','ORB','DRB','RPG','APG','SPG','BPG','PPG']

for tr in trs[1:]:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '').strip() for td in tds]
    rows.append(row)

df = pd.DataFrame(rows, columns=columns)
df.to_csv('Player Stats.csv', index=False)
