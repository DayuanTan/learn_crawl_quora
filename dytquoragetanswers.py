import requests
from bs4 import BeautifulSoup
#import re

questionstitlelist = ['questionstitlelist']
questionsanswers = ['questionsanswers']

fh = open('questionslinks.txt')
for link in fh:
    print('\nA new link: ',link.rstrip())
    if link < 'questionslinks':
        s= requests.Session()
        url=link.rstrip()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        url_htm = s.get(url, headers = headers)
        soup = BeautifulSoup(url_htm.text, "html.parser")
        print("hello.")

        for line in soup.findAll('div',{'class:','_type_serif_title_large'}):
            print('title:',line.string)
            questionstitlelist.append(line.string)
            questionsanswers.append(line.string)

        for line in soup.find('span',{'class:','ui_qtext_rendered_qtext'}):
            soup2 = BeautifulSoup(str(line))
            for line2 in soup2.findAll('p',{'class:','ui_qtext_para'}):
                print('line2:',line2)
                print('str(line2):',str(line2))
                soup3 = BeautifulSoup(str(line2))
                while soup3.p.br:
                    print('soup3.p.br',soup3.p.br.unwrap())
                    print('soup3.p.br:',soup3.p)
                while soup3.p.i:
                    print('soup3.p.i',soup3.p.i.unwrap())
                    print('soup3.p.i:',soup3.p)
                while soup3.p.b:
                    print('spup3.p.b',soup3.p.b.unwrap())
                    print('soup3.p.b:', soup3.p)
                while soup3.p.span:
                    print('spup3.p.span',soup3.p.span.unwrap())
                    print('soup3.p.span:', soup3.p)
                while soup3.p.a:
                    print('spup3.p.a',soup3.p.a.unwrap())
                    print('soup3.p.a:', soup3.p)
                answer = BeautifulSoup(str(soup3.p)).find('p').string
                #answer = str(BeautifulSoup(str(soup3.p)).find('p'))
                print('---answer:',answer)
                questionsanswers.append(answer)
        questionsanswers.append('\n')

        with open('questionstitlelist.txt','w',encoding='utf-8') as f:
            for i in range(len(questionstitlelist)):
                print(i," ",questionstitlelist[i])
                f.write(questionstitlelist[i]+'\n')

        with open('questionsanswers.txt','w',encoding='utf-8') as f:
            for i in range(len(questionsanswers)):
                f.write(questionsanswers[i]+'\n')
        print('End.')