import requests
from bs4 import BeautifulSoup
import re

questionList = []
answerList = []

#build training data header
with open('ethereum.yml','w',encoding='utf-8') as f:
    f.write('categories:\n')
    f.write('- ethereum\n')
    f.write('conversations:\n')

fh = open('ethereum_questions.txt')
for link in fh:
    if link < 'questionslinks':
        s= requests.Session()
        url='https://www.quora.com'+link.rstrip()
        print("url:", url)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        url_htm = s.get(url, headers = headers)
        #print("response:", url_htm.text)
        soup = BeautifulSoup(url_htm.text, "html.parser")

        question = ''
        for line in soup.findAll('div',{'class:','_type_serif_title_large'}):
            if line.string != '':
                question = line.string
                exit

        answer_length = 0
        answer = ''
        for line2 in soup.findAll('p',{'class:','ui_qtext_para'}):
            if line2.string:
                answer_length = answer_length + len(line2.string)
                if (answer_length > 500 and answer != ''):
                    break
                else:
                    answer += line2.string + ' ';

        if question != '' and answer != '':
            question = re.sub('[\'\"\(\)\:]', '', question)
            answer = re.sub('[\'\"\(\)\:\-\*\t]', '', answer)
            answer = answer.replace("&", "and")

            with open('ethereum.yml','a+',encoding='utf-8') as f:
                f.write('- - ' + question + '\n')
                f.write('  - ' + answer + '\n')

