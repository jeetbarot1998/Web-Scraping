from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Firefox()
driver.get("https://www.skyscanner.co.in/transport/flights/bom/in/200804/200811/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&rtn=1")
htm=driver.find_element_by_id("destinations")
htm.tag_name
htm.text
htm.get_attribute("innerHTML")
soup= BeautifulSoup(htm.get_attribute("innerHTML"),features="lxml")
#print(soup.prettify())

containers = soup.find_all('div', class_="browse-data-entry trip-link")
#for c in containers: 
 #   print(c)

#for name in containers: 
 #   print(name.find_all('h3'))  # GIVES NAME OF ALL THE CITIES

i=0
for name in containers: 
    print(name.text.strip())
    i +=1
    print(i)  # GET ALL PERFECT

#for name in containers: 
 #   print(name.find_all('class="flightLink visible"'))  # GET ALL links

