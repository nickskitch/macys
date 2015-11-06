#ScriptName : Login.py
#---------------------
import os
from selenium import webdriver
import time
#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass





baseurl = "http://mdc2vr4073:9090/MacysOrchestration/home.html"
username = USERNAME
password = PASS1

xpaths = { 'usernameTxtBox' : "//input[@name='userLogin.username']",
           'passwordTxtBox' : "//input[@name='userLogin.password']",
           'submitButton' :   "//input[@value='Log In']",
           'environmentName' : "//input[@name='orchestrationHomeBO.selSrearchEnvName']",
           'fromDate' : "//input[@name='orchestrationHomeBO.fromDate']",
           'toDate' : "//input[@name='orchestrationHomeBO.toDate']",
           'submitButton2' :   "//input[@value='  Search  ']",

         }

chromedriver = "/Users/Nick/Desktop/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
mydriver = webdriver.Chrome(chromedriver)
mydriver.get(baseurl)
mydriver.maximize_window()

#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

mydriver.find_element_by_xpath(xpaths['environmentName']).send_keys('mcominternal5024')

beginDate=time.strftime("%m-01-%Y")
endDate=time.strftime("%m-28-%Y")

mydriver.find_element_by_xpath(xpaths['fromDate']).send_keys(beginDate)

mydriver.find_element_by_xpath(xpaths['toDate']).send_keys(endDate)

mydriver.find_element_by_xpath(xpaths['submitButton2']).click()



