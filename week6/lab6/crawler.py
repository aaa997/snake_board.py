import sys
import requests
import bs4
parsmeters = sys.argv
url = parsmeters[1]

response = requests.get(url)

html = response.text

soup = bs4.BeautifulSoup(html)

paragraphs = soup.find_all("p")

for p in paragraphs:
     links = p.find_all("a")
     for link in links:
         target = link.get("href")
         good_link ='https://www.wikipdia.org'+target
         print(good_link)


