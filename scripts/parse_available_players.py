import requests
from bs4 import BeautifulSoup


def main():
    params = {
                "sort": "PTS",
                "sdir": "1",
                "status": "A",
                "pos": "DEF", # Update to 'O' to pull in offensive players
                "stat1": "S_PS_2024"
            }

    # Send a GET request to the URL
    response = requests.get("https://football.fantasysports.yahoo.com/f1/1322308/players", params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first table on the page
        table = soup.find('table')

        # Use the second header row as keys
        header_rows = table.find_all('thead')[0].find_all('tr')
        headers = [th.get_text(strip=True).replace('\ue002', '').lower() for th in header_rows[1].find_all('th') if th]
        headers[1] = 'player_name'

        # Extract rows of data
        rows = []
        for tr in table.find('tbody').find_all('tr'):
            cells = [td.get_text(separator='\n').lstrip().split('\n')[0] for td in tr.find_all('td')]
            if cells:  # only add non-empty rows
                # Create a dictionary only with headers that have valid keys
                row_data = {headers[i]: cells[i] for i in range(len(headers)) if headers[i]}
                rows.append(row_data)

        return rows

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
