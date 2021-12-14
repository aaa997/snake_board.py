
import requests
import bs4

response = requests.get('https://he.wikipedia.org/wiki/סאלאר_דה_אויוני')

html = response.text

soup = bs4.BeautifulSoup(html)

paragraphs = soup.find_all("p")

for p in paragraphs:
     links = p.find_all("a")