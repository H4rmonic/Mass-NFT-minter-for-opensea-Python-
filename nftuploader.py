#!/usr/bin/python

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

EXTENSION_PATH = 'meta.crx'
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)


driver = webdriver.Chrome(chrome_options=opt)

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/button').click()
driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
driver.find_element_by_xpath('//button[text()="No Thanks"]').click()

time.sleep(2)


SECRET_RECOVERY_PHRASE=('metamask recovery phrase')
NEW_PASSWORD=('SuperSecureP4ss')

secret = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input')
secret.send_keys(SECRET_RECOVERY_PHRASE)

new = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input')
new.send_keys(NEW_PASSWORD)

confirm = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input')
confirm.send_keys(NEW_PASSWORD)


driver.find_element_by_css_selector('.first-time-flow__terms').click()
driver.find_element_by_xpath('//button[text()="Import"]').click()

time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/button').click()

time.sleep(3) 
driver.find_element_by_xpath('/html/body/div[2]/div/div/section/header/div/button').click()

print("Done signing into metamask, opening opensea...") 

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://opensea.io/asset/create')
time.sleep(3)
main_page = driver.current_window_handle

driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[1]/button/div[2]').click()
time.sleep(3) 
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
         
# change the control to signin page       
driver.switch_to.window(login_page)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
time.sleep(5)



print("Done signing into opensea, creating first nft...") 

driver.switch_to.window(main_page)






nft_number = 105

Desc = ("Your description here")

#For lis, create a list of numbers equal to the number of pictures you have to upload, IE if you have 10 pictures the list below should work
#if you have many nft's to upload these websites will be of use to you: Generate list of numbers: https://numbergenerator.org/numberlist format with commas: https://convert.town/replace-spaces-with-commas
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nft_number = 2957
 
while(nft_number < len(lis)):
    print(lis[nft_number], end = " ")
     
    # Changing the value of
    # i inside the loop will
    # change it's value at the
    # time of checking condition
    nft_number += 1
    print("nft ", nft_number, " Start")

    #Image
    s = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/section/div/form/div[1]/div/div[2]/input")
    #file path specified with send_keys
    s.send_keys("/home/owo/Desktop/nftscript/nfts/",nft_number,".png")





    #Name
    nftname = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/section/div/form/div[2]/div/div[2]/div[1]/input')
    nftname.send_keys('nfts Collection #', nft_number)

    #Description 
    Description = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/section/div/form/div[4]/div/textarea')
    Description.send_keys(Desc)
    
    #collectoin
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/section/div/form/div[5]/div/div[2]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/section/div/form/div[5]/div/div[3]').click()
    
    
    #create
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/section/div/form/div[9]/div[1]/span/button').click()

    #start again 
    time.sleep(2)
    driver.get('https://opensea.io/asset/create') 
    time.sleep(6)








