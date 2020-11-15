from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import os

# taking user input
print("What do you want to download?")
download = input()
site = 'https://www.google.com/search?tbm=isch&q=' + download

# providing driver path
current = os.getcwd()
driver = webdriver.Firefox(executable_path=current + r'\geckodriver.exe')

# passing site url
driver.get(site)


# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


# below while loop scrolls the webpage 10 times(if available)

i = 0

while i < 10:
    # for scrolling page
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    try:
        # for clicking show more results button
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
    except Exception as e:
        pass
    time.sleep(5)
    i += 1

# parsing
soup = BeautifulSoup(driver.page_source, 'html.parser')

# closing web browser
driver.close()

# scraping image urls with the help of image tag and class used for images
img_tags = soup.find_all("img", class_="rg_i")

os.makedirs(current + '/' + str(download))
complete_name = os.path.join(current + '\\'+ str(download) + '\\')

count = 0
for i in img_tags:
    # print(i['src'])
    try:
        # passing image urls one by one and downloading

        urllib.request.urlretrieve(i['src'],   complete_name + str(count) + ".jpg")
        count += 1
        print("Number of images downloaded = " + str(count), end='\r')
    except Exception as e:
        #print('nothing worked')
        pass
