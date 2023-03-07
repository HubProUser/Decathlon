import bs4
import urllib.request
import re


def request(link):     # get decathlon site code
    r = urllib.request.urlopen(link+'sports')
    soup = bs4.BeautifulSoup(r, 'html.parser')
    return soup


def sports(soup):
    links = []
    div = soup.find('div', {'class': 'container-fluid'}).find('ul')
    for link in div.find_all('a', href=True):
        links.append('https://www.sportdepot.bg/'+link['href'])
    return links


data = request(link='https://www.sportdepot.bg/')
sports = sports(data)
print(sports)

