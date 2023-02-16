import bs4
import urllib.request


def get_links(a):
    decathlon = 'https://www.decathlon.bg'
    r = urllib.request.urlopen(decathlon)
    soup = bs4.BeautifulSoup(r, 'html.parser')
    link = soup.find('li', {'class': f'root root-{a}'}).find('a')['href']
    return link


def links():
    men_stocks = get_links(a='4')
    women_stocks = get_links(a='5')
    children_stocks = get_links(a='6')
    accessories = get_links(a='7')
    return men_stocks, women_stocks, children_stocks, accessories







