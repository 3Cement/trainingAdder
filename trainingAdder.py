#! python3
# TrainingAdder.py - The program that automatically logging into Endomondo website.
# Then find the latest training on the hard drive and add that to the Endomondo profile

import time, webbrowser, pdb
from selenium import webdriver

browser = webdriver.Chrome(r'C:\Users\Daniel\MyPythonScripts\webdrivers\chromedriver_win32\chromedriver.exe')
browser.get('https://www.endomondo.com/login?returnUrl=~2Fhome')
#time.sleep(5) # Let the user actually see something!

emailElem = browser.find_element_by_name('email')
emailElem.send_keys('danielmilewski123@gmail.com')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('mojetreningi123')
passwordElem.submit()

time.sleep(1)
browser.get('https://www.endomondo.com/workouts/create')

fileImport = browser.find_element_by_class_name('fileImport')
fileImport.click()

path = u'//a[text()="Choose File"]'

time.sleep(1)
#pdb.set_trace()
try:
	fileUpload = browser.find_element_by_xpath(path).click()
except Exception as exc:
	print('There was a 1st problem: %s' % (exc))
try:
	fileUpload = browser.find_element_by_class_name(path).click()
except Exception as exc:
	print('There was a 2nd problem')
try:
	fileUpload = browser.find_element_by_css_selector(path).click()	
except Exception as exc:
	print('There was a 3rd problem')
try:
	fileUpload = browser.find_element_by_id(path).click()	
except Exception as exc:
	print('There was a 4th problem')
try:
	fileUpload = browser.find_element_by_link_text(path).click()	
except Exception as exc:
	print('There was a 5th problem')
try:
	fileUpload = browser.find_element_by_partial_link_text(path).click()	
except Exception as exc:
	print('There was a 6th problem')
try:
	fileUpload = browser.find_element_by_name(path).click()	
except Exception as exc:
	print('There was a 7th problem: %s' % (exc))
try:
	fileUpload = browser.find_element_by_tag_name(path).click()	
except Exception as exc:
	print('\n' + path)
