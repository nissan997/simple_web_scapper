from bs4 import BeautifulSoup
import requests

source = requests.get('http://prothomalo.com').text
soup = BeautifulSoup(source,'lxml')
count=0
for articles in soup.find_all('span',class_='title'):
    print(articles.text)
    print("")
    count = count + 1
print("Found "+ str(count) + " headlines")