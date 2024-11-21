import re
import requests
from bs4 import BeautifulSoup


def main():
    response = requests.get('https://football.fantasysports.yahoo.com/f1/gamedaycalls')

    soup = BeautifulSoup(response.content, 'lxml')

    table = soup.find('table', id='gamedayscalltable')
    headers = [heading.text for heading in table.find_all('th')]

    table_rows = [row for row in table.find_all('tr')]

    results = [{headers[index]: cell.text for index, cell in enumerate(row.find_all("td"))} for row in table_rows]
    results = [result for result in results if result]

    for result in results:
        for i, v in result.items():
            for substring in ['\n', ' No new player Notes', ' Player Note', ' New']:
                v = v.replace(substring, '')
            result[i] = v

        try:
            name_pattern = r'[A-Z][^A-Z]*'
            result['Name'] = ' '.join(re.findall(name_pattern, result['Name'])[:2]).strip()
            result['Name'] = re.sub(r'\s+', ' ', result['Name'])
            result['Team'] = result.pop('Depth Chart')
        except Exception as e:
            print(e)

    return results
