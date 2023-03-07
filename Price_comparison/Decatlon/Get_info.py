import bs4
import urllib.request
import re


def request(link):     # get decathlon site code
    r = urllib.request.urlopen(link)
    soup = bs4.BeautifulSoup(r, 'html.parser')
    return soup


def sports(soup):
    div = soup.find('div', {'class': 'container-fluid'})
    ul = div.find('ul', {'class': 'list-unstyled'})
    return ul


data = request(link='https://www.sportdepot.bg/sports')
sports = sports(data)
print(sports)

