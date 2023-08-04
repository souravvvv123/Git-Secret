import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import argparse
import termcolor
from termcolor import colored

banner = colored('''--------------------------------------------------------------------------

###############   #####  ###########        ##########  #########  #########  ########  #########  ############                
#                   #         #             #           #          #          #      #  #               #
#                   #         #             #           #          #          #      #  #               #
#                   #         #  ------     #           #          #          #      #  ########        #
#        ######     #         #             ##########  #########  #          ########  #               #
#        #    #     #         #                      #  #          #          # #       #               #
#        #    #     #         #                      #  #          #          #   #     #               #
##########    #   #####       #             ##########  #########  ########## #     #   ########        #                    

                                                                            AUTHOR: SOURAV CHAKRABORTY
                                                                            VERSIONl:l 0.1        
---------------------------------------------------------------------------------''', '''red''')

print(banner)

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str, help='Enter the url to begin search')
args = parser.parse_args()


s = Service(ChromeDriverManager(version="114.0.5735.90").install())
driver = webdriver.Chrome(service=s)
#url = "https://github.com/freepein"
url=args.url
url2 = url + "?tab=repositories"
driver.get(url2)
names=[]
res = driver.find_elements(By.CLASS_NAME, "wb-break-all")
for heading in res:
    x=heading.text
    y=x.replace("Public","")
    z=names.append(y)

time.sleep(1)
my_list = []


def loop(my_list):
    driver.get(my_list)
    time.sleep(1)
    driver.back()


for i in res:
    i = url + "/" + i.text
    i = i.replace("Public", "")
    my_list.append(i)

url_content=[]
for j in my_list:
    alllinks = driver.get(j)
    time.sleep(1)
    alllinks2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in alllinks2:
        getting = a.text
        getting = getting.replace(" ", "") # remove whitespace
        url_content.append(getting)



url_heading=[]
whole_content=[]
def getting_url_heading():
    for title in names:
        global finale
        tit=url+"/"+title
        finale=url_heading.append(tit)
def parsing_url_heading():
    for parse in url_heading:
        for cont in url_content:
            aa=parse+"/"+"blob/master/"+cont
            bb=whole_content.append(aa)


getting_url_heading()
parsing_url_heading()

listed_urls = [url.replace(" ", "") for url in whole_content] # remove whitespace

working_urls=[]
for work in listed_urls:
    try:
        req=requests.get(work.strip())
        print(f"status code for {work}: {req.status_code}")
        if req.status_code==200:
            working_urls.append(work)
    except requests.exceptions.RequestException as ee:
        print(f"Error getting {work}: {ee}")

print(f"working urls are: {working_urls}")

def read_keywords_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


keywords_filename = 'keyword.txt'
keywords = read_keywords_from_file(keywords_filename)


def check_keywords_in_content(url, keywords):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        for keyword in keywords:
            if keyword in content:
                return keyword
    return None


for url in working_urls:
    found_keyword = check_keywords_in_content(url, keywords)
    if found_keyword:
        print(f"Keyword '{found_keyword}' found in URL: {url}")



driver.quit()
