import requests
from bs4 import BeautifulSoup
# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys 
import time
 
page = requests.get('https://isthereanydeal.com') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
 

#listie = soup.find("a", string = "Patrick's Parabox")

#print(listie)

game_name = "patricksparabox"


all_divs = soup.find('a', {'data-evt' : '["shop","click","%s"]'%(game_name)})
try: 
    rest = all_divs.find_all_next('a', {'data-evt' : '["shop","click","%s"]'%(game_name)})
    print(rest[len(rest)-1].text)
except: 
    rest = all_divs
    print(rest.text)
