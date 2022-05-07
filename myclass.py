from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
#from PIL import Image

browser1=webdriver.Chrome()
browser1.get("https://myclass.lpu.in")
browser1.maximize_window()
userid="12011977    "
password="Gkp@123"

#entering user id and password
browser1.find_element_by_xpath("/html/body/div[2]/div/form/div[6]/input[1]").send_keys(userid)
browser1.find_element_by_xpath("/html/body/div[2]/div/form/div[6]/input[2]").send_keys(password)

#click log in button
browser1.find_element_by_xpath("/html/body/div[2]/div/form/div[7]/button").click()
#view classes
browser1.find_element_by_xpath("/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a").click()

time.sleep(5)


cls=1
#click a particular class
try:
    browser1.find_element_by_xpath("/html/body/div[1]/div[6]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a["+str(cls)+"]/div").click()
except:
    browser1.send_keys(Keys.SPACE)
    browser1.find_element_by_xpath("/html/body/div[1]/div[6]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[5]/div").click()

time.sleep(2)

#click on join button
browser1.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/a").click()

time.sleep(30)

try:
    print("level 1 reached")
    audio1=browser1.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i")
    print("level 2 reached")
    audio1.click()
    print("level 3 reached")
    print("audio btn found")
    print("level 4 reached")
    audio1.click()
    print("level 5 reached")
except:
    print("level 6 reached")
    print("audio btn NOT found")
    print("level 7 reached")













#join audio
# for i in range(150):
#     try:
#         clkAudioBtn=browser1.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]").click()
#         print("checked for audio")
#       #  /html/body/div[5]/div/div/div[1]/div/div/span/button[2]/span[1]/i     audio 
#         print("audio clicked successfully")
        
#     except:
#         time.sleep(0.1)
#         print("exception reached")
# /html/body/div[31]/div/div/div[1]/div/div/span/button[2]/span[1]/i
# /html/body/div[30]/div/div/div[1]/div/div/span/button[2]/span[1]/i
# /html/body/div[31]/div/div/div[1]/div/div/span/button[2]/span[1]/i
# /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i

# /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i
# /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i
# /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]

# /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]
# /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]


# for k in range(60):
#     try:
#         clkAudioBtn=browser1.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]").click()
#         print("audio btn found")
#     except:
#         print("audio btn not found")
#         time.sleep(1)
#                                           /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i  inside small
#                                           /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i
#                                           /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i
#                                           /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i
                                        #   /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i
                                            # /html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i

#click on poll


for i in range(1000000000):
    try:
        browser1.find_element_by_xpath("/html/body/div[1]/main/div[1]/div/span[2]/div/div[2]/button").click()
        print("poll clicked successfully")
    except:
        time.sleep(2)
        print("no poll yet")



# /html/body/div[1]/main/div[1]/div/span[2]/div/div[2]/button