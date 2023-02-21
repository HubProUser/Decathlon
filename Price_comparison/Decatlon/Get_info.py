import bs4
import urllib.request
import gspread


def decathlon():
    link = 'https://www.decathlon.bg/'
    r = urllib.request.urlopen(link)
    soup = bs4.BeautifulSoup(r, 'html.parser')
    return soup


def category(soup):
    categories = soup.find_all('ul', {'class': 'submenu submenu-depth-2'})
    return categories













data = decathlon()
links = category(data)
sport = sports(links)
print(sport)
