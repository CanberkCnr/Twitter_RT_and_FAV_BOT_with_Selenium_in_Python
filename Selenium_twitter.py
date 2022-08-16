from ast import While
from asyncio import wait_for
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import BaseWebElement,WebElement
import Selenium_twitter_pass
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)
browser.get("https://www.twitter.com/login")


def loginusername():

    username_get = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
    username_get.send_keys(Selenium_twitter_pass.kullanici)

    time.sleep(2)
    login_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
    login_button.click()

loginusername()

def loginpassword():
    password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password.send_keys(Selenium_twitter_pass.password)
    last_clickforlogin = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
    last_clickforlogin.click()
    time.sleep(5)

loginpassword()

def search_button():
    browser.get("https://twitter.com/explore")
    browser.maximize_window()
    wait_for_search = WebDriverWait(browser, 30)
    search_wait = wait_for_search.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")))
    search_wait.send_keys("#Ataturk")
    search_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
    search_button.send_keys(u'\ue007')

    time.sleep(5)

search_button()

def scroll():

    lenofPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenofPage = document.body.scrollHeight;return lenofPage;")

    match = False
    while(match == False):
        lastCount = lenofPage

        time.sleep(3)
        lenofPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenofPage = document.body.scrollHeight;return lenofPage;")

        if lastCount == lenofPage:

            match=True
    time.sleep(5)
scroll()

def scrool_times():
    for i in range(1,5):
        lenofPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenofPage = document.body.scrollHeight;return lenofPage;")
        time.sleep(3)
scrool_times()

def tweetcek():
    tweetlist = []
    for i in range(0,3):
        get_value_of_search = browser.find_elements(By.CSS_SELECTOR, ".css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")[i].text

        tweetlist.append(get_value_of_search)
    
    tweetCount = 1
    with open("tweets.txt","w",encoding="UTF-8") as file:
        for entry in tweetlist:
            file.write(str(tweetCount) + ".\n"+ entry + "\n")
            file.write("\n*************************************************\n")
            tweetCount += 1
tweetcek()

def likebutton():
    like_button = browser.find_elements(By.XPATH, "//div[@data-testid = 'like']")
    for like in like_button:
        like.click()
        time.sleep(5)
likebutton()

time.sleep(5)

def rt():
    rtlist = []
    rt_button = browser.find_elements(By.XPATH, "//div[@data-testid = 'retweet']")
    for rt in rt_button:
        rt.click()
        rt_button_confirm = browser.find_element(By.XPATH, "//div[@data-testid = 'retweetConfirm']")
        rt_button_confirm.click()
        time.sleep(5)
rt()

time.sleep(5)

browser.close()


