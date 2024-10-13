import requests
from bs4 import BeautifulSoup

#request to the website
url = 'https://news.ycombinator.com/'
html = requests.get(url)

#parse the html content 
soup = BeautifulSoup(html.content, "html.parser")

#get all the news headers
incomplete_headers = soup.find_all('span', class_="titleline")

#isolate the title and print out with a number
for i, incomplete_header in enumerate(incomplete_headers):
    link_header = incomplete_header.find('a')
    title_of_header = link_header.text
    number = i + 1
    print(f"{number}. {title_of_header} ")
