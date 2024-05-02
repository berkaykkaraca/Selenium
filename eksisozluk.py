from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
browser = webdriver.Firefox()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"
PageCount = 1
entries = []
entryCount = 1
while PageCount<11:
    randomPage = random.randint(1,2657)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    contents = browser.find_elements(By.XPATH,"div.content")
    for content in contents:
    
        entries.append(content.text)
    time.sleep(2)
    PageCount+=1

with open("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+ ".\n"+entry+"\n")
        file.write("**********************************\n")
        entryCount+=1

browser.close()



"""  Scroll Code
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)


     """