import bs4
import requests

r = requests.get('https://www.decathlon.bg/')

soup = bs4.BeautifulSoup(r.text, 'lxml')

titles = soup.find_all('div', {'class': 'title'})

print(titles)
