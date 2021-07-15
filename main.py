import requests
import bs4
import re

header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36 '
}

url = 'https://store.steampowered.com/explore/new/'

r = requests.get(url, header)
soup = bs4.BeautifulSoup(r.text,"html.parser")
