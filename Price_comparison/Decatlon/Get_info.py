import bs4
import urllib.request


def request(link):
    r = urllib.request.urlopen(link+'sports')
    soup = bs4.BeautifulSoup(r, 'html.parser')
    return soup


def sport_links():
    soup = request('https://www.sportdepot.bg/')
    names = []
    links = []
    div = soup.find('div', {'class': 'container-fluid'}).find('ul')
    for link in div.find_all('a', href=True):
        links.append('https://www.sportdepot.bg/'+link['href'])
    for name in div.find_all('a'):
        names.append(name.text)
    names = [x.lower() for x in names]
    paired = dict(zip(names, links))
    return paired, names


def choose_what_to_do():
    pass


def choose_sport():
    pass


def stock_info():
    pass


def end_program():
    pass


def get_stock_info():
    while True:
        choose_what_to_do()
        if choose_sport():    # start process
            stock_info()
            choose_what_to_do()
        else:
            end_program()     # break


choose_sport()

