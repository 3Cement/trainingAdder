#! python3
# TrainingAdder.py - The program that automatically logging into Endomondo website.
# Then find the latest training on the hard drive and add that to the Endomondo profile

import time, webbrowser, pdb, glob, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Finding the lates added file in the folder:
list_of_files = glob.glob("C:\\Users\\Daniel\\OneDrive\\Moje treningi\\*.gpx")
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

browser = webdriver.Chrome(r'C:\Users\Daniel\MyPythonScripts\webdrivers\chromedriver_win32\chromedriver.exe')
browser.get('https://www.endomondo.com/login?returnUrl=~2Fhome')
#browser.maximize_window()
time.sleep(1)

emailElem = browser.find_element_by_name('email')
emailElem.send_keys('******')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('******')
passwordElem.submit()
time.sleep(1)

browser.get('https://www.endomondo.com/workouts/create')

fileImport = browser.find_element_by_class_name('fileImport')
fileImport.click()

time.sleep(1)
browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
time.sleep(1)

try:
	element = browser.find_element_by_name("uploadFile")
	#element.click()
	element.clear()
	time.sleep(1)
	element.send_keys(latest_file)
except Exception as exc:
	print('There was a problem: %s' % (exc))

try:
	uploadFile = browser.find_element_by_name("uploadSumbit").click()
except Exception as exc:
	print('There was a problem: %s' % (exc))

time.sleep(1)
try:
	nextUpload = browser.find_element_by_name("reviewSumbit").click()
except Exception as exc:
	print('There was a problem: %s' % (exc))
