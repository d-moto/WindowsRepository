import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service

#WEBブラウザの起動
driver = webdriver.Chrome() 

#自動ログインしたいウェブサイトのURLをコピペ
driver.get('https://www.google.com/?hl=ja') 

#ウェブサイトの起動を確認するため
time.sleep(10)