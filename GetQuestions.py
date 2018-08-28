from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

questionslinks = []

driver = webdriver.Chrome()
driver.get("http://www.quora.com/search?q=ethereum")
#driver.get("http://www.quora.com/search?q=bitcoin")
#driver.get("http://www.quora.com/search?q=cryptocurrency")

count = 0
#get 300 pages
while (count < 300):
  count = count + 1
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(1.5);

soup = BeautifulSoup(driver.page_source, "html.parser")

for line in soup.findAll('div',{'class:','e_col w4_5'}):
    soup2 = BeautifulSoup(str(line), "html.parser")
    for line2 in soup2.findAll('div',{'class:','title '}):
        q_url = BeautifulSoup(str(line2), "html.parser").find('a').get('href')
        if q_url.startswith('/unanswered'):
            continue
        else:
            questionslinks.append(q_url)

driver.close()

with open('ethereum_questions.txt','w',encoding='utf-8') as f:
    for i in range(len(questionslinks)):
        f.write(questionslinks[i]+'\n')

