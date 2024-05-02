from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
browser = webdriver.Firefox()
url = "https://ankarateknokent.com/firmalar-portfolio/"
entries = []
entryCount = 1
browser.get(url)
contents = browser.find_elements(By.CSS_SELECTOR,"div.fg-item-content")
for content in contents:
    
        entries.append(content.text)
time.sleep(2)

with open("deneme.txt","w",encoding="UTF-8") as file:
        for entry in entries:
                file.write(str(entryCount)+ ".\n"+entry+"\n")
                file.write("**********************************\n")
                entryCount += 1

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