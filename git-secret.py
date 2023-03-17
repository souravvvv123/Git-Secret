import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
scrape=input("what page would you like to scrape?")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get(f"{scrape}")
repo=f"{scrape}"
res=driver.find_elements(By.CLASS_NAME,"repo")

repo_links=[]
flink=[]

def going_for_raw(second_page):
    driver.get(second_page)
    raw=driver.find_element(By.CLASS_NAME,"js-permalink-replaceable-link")
    raw.click()
    htmll=driver.page_source
    htmll=f"{htmll}"
    if "password" in htmll:
        print(f"found password:{second_page}")
    elif "api_key" in htmll:
        print(f"found api_key:{second_page}")
    elif "admin" in htmll:
        print(f"found admin in:{second_page}")
    elif "secret_token" in htmll:
        print(f"found secret token:{second_page}")
    else:
        print("couldnt find any secret")

def loop(next_page):
    global a
    driver.get(next_page)
    res2=driver.find_elements(By.CLASS_NAME,"js-navigation-open")
    if "py" in a.text:
        second_page=f"{next_page}/blob/master/{a.text}"
        going_for_raw(second_page)

for i in res:
    rep=i.text.replace("Public","").strip()
    repo_links.append(rep)

for l in repo_links:
    next_page=f"{repo}/{l}"
    flink.append(next_page)
    loop(next_page)
driver.quit()





