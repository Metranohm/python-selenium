from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)