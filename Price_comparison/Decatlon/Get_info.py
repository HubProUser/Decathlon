import bs4
import urllib.request
import re


def request(link):
    r = urllib.request.urlopen(link)
    soup = bs4.BeautifulSoup(r, 'html.parser')
    return soup


def category(soup):
    categories = soup.find_all('li', {'class': 'root root-3 category-sports'})
    return categories


def sports(categories):
    for sport in categories:
        sport = sport.find_all('a', href=re.compile('https://www.decathlon.bg/'))
        return sport


data = request(link='https://www.decathlon.bg/')
cat = category(data)
sport = sports(cat)
print(sport)

