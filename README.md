# learn_crawl

This is what I did when I tried to learn sth about crawling. 

I try to crawl questions and first answer form Quora. I use BeautifulSoup 4.

- quoragetquestionlinks.py is used to get question links under one key word. In my case, I chose "cryptocurrency" and "bitcoin".Those questions links will be stored in questionslinks.txt.
- quoragetanswers.py is used to get questions titles and first answers form quora. It will visit each links form questionslinks.txt, and then get the titles and answers. All titles will be stored in questionstitlelist.txt and all first answers will be store in questionsanswers.txt.

One issue is that Quora uses AJAX to flip pages so I can only get 10 questions in quoragetquestionlinks.py. Some lib, like Selenium may can solve this issue. I will try to figure it out later. 

<br><br>
\------<br>
\* Thanks to Jack Shan, who helps me to pick up BeautifulSoup 4 quickly. Part of my code also reference his code in https://github.com/Jackustc/Simpledataclawer.
