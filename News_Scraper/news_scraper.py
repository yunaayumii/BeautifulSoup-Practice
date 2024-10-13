import requests
from bs4 import BeautifulSoup

#request to the website
url = 'https://news.ycombinator.com/'
html = requests.get(url)

#parse the html content 
soup = BeautifulSoup(html, "html.parser")

