from selenium import webdriver
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

driver = webdriver.Firefox()
driver.get("https://www.yatra.com/domestic-flights/flights-from-mumbai.html")
htm=driver.find_element_by_id("flightResults")

soup= BeautifulSoup(htm.get_attribute("innerHTML"),features="lxml")
t=soup.find_all('div') 
for name in t:
    print(name.get('data-departdate'))
    print(name.get('data-arrivalcity'))
    print(name.get('data-flightprice'))
    
