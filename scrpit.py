from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import json

# url = "https://auto.ru/"
# src = requests.get(url)
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src.text)

def getHrefs():
    with open("index.html", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    items=soup.find_all(class_="IndexMarks__item")
    allMarks = {}
    for item in items:
        markName = item.find(class_="IndexMarks__item-name").text
        markHref = item.get("href")
        allMarks[markName]=markHref
    with open("allMarks.json", "w", encoding="utf-8") as file:
        json.dump(allMarks, file, indent=4, ensure_ascii=False)


def getInfo():
    with open("7_Ford.html", encoding="utf-8") as file:
        ford=file.read()
    soup=BeautifulSoup(ford, "lxml")
    allTitles = soup.find_all(class_="ListingItemTitle_link")
    for title in allTitles:
        print(title.text)
    

def getData():
    with open("allMarks.json", encoding="utf-8") as file:
        allMarks = json.load(file)

    for markName, markHref in allMarks.items():
        count = 0
        if count == 0:
            req = requests.get(url=markHref)
            src = req.text
            with open(f"data\\{count}_{markName}.html", "w", encoding="utf-8") as file:
                file.write(src)
            getInfo()
            count += 1
            
            


try:
    getHrefs()
except Exception as ex:
    print(ex)
finally:
    print("Success")