import bs4
import urllib.request


def request(link):     # get decathlon site code
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
    paired = dict(zip(names, links))
    return paired, names


def choose_sport():
    paired, names = sport_links()
    while True:
        print(names)
        input_name = input('Choose category:\n')
        if input_name in names:
            print(paired[input_name])
            break
        else:
            print('no such category')


choose_sport()

