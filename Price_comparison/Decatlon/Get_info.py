import bs4
import urllib.request
import gspread
import re
from urlextract import URLExtract
import ast


def decathlon():
    link = 'https://www.decathlon.bg/'
    r = urllib.request.urlopen(link)
    soup = bs4.BeautifulSoup(r, 'html.parser')
    return soup


def category(soup):
    categories = soup.find_all('li', {'class': 'root root-3 category-sports'})
    return categories


def sports(categories):
    for sport in categories:
        sport = str(sport.find_all('a'))
        return sport


extractor = URLExtract()


def link(sport):
    for url in extractor.gen_urls(sport):
        links = url
        print(links)



data = decathlon()
cat = category(data)
sport = sports(cat)
links = link(sport)
link()
