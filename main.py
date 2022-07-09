import time
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
urls = []
titles = []
for i in range(1,48):
    driver.get("https://leetcode.com/problemset/all/?page=" + str(i))

    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    all_ques_div = soup.findAll("div", {"class": "truncate overflow-hidden"})

    all_ques = []  # will contain all ques anchor tag
    for ques in all_ques_div:
        all_ques.append(ques.find("a"))

    for ques in all_ques:
        urls.append("https://leetcode.com" + ques['href'])
        titles.append(str(ques.text.encode("utf-8")))

with open("leetcode_problem_urls.txt", "w+") as f:
    f.write('\n'.join(urls))

with open("leetcode_problem_titles.txt", "w+") as f:
    f.write('\n'.join(titles))

cnt = 0
for url in urls:
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    problem_text = soup.find('div', {"class": "content__u3I1 question-content__JfgR"})
    cnt += 1
    if problem_text==None:
        print(cnt)
        continue

    main_text = problem_text.get_text()
    main_text = main_text.encode("utf-8")
    main_text = str(main_text)

    with open("leetcode_problem_statement" + str(cnt) + ".txt", "w+") as f:
        f.write(main_text)