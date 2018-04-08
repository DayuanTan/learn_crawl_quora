import requests
from bs4 import BeautifulSoup   
#import re

questionslinks = ['questionslinks']

s= requests.Session()
#url='https://www.quora.com/search?q=cyptocurrency'
url='https://www.quora.com/search?q=bitcoin&type=question'
headers = {'method': 'GET',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Connection': 'Keep-Alive',
           'cache-control': 'max-age=0',
           'Range': 'bytes=0-100000',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
url_htm = s.get(url, headers = headers)
soup = BeautifulSoup(url_htm.text, "html.parser")
print("hello.")

for line in soup.findAll('div',{'class:','e_col w4_5'}):
    soup2 = BeautifulSoup(str(line))
    for line2 in soup2.findAll('div',{'class:','title '}):
        q_url = BeautifulSoup(str(line2)).find('a').get('href')
        print(q_url)
        if q_url.startswith('/unanswered'):
            continue
        else:
            questionslinks.append('https://www.quora.com'+q_url)


with open('questionslinks.txt','w',encoding='utf-8') as f: 
    for i in range(len(questionslinks)):
        f.write(questionslinks[i]+'\n')