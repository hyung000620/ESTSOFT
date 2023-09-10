from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import math

# 내 아이디, 패스워드, 검색할 회사
USER_ID = "dksms55@daum.net"
PWD = "1q2w3e4r"
QUERY = "이스트소프트"


# 1. 로그인
def login(driver, user_id, pwd):
    driver.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")
    
    # 카카오 로그인 시도 안되네...
    time.sleep(3)
    kakao = driver.find_element(By.CLASS_NAME, "btn_signup_kakao")
    kakao.click()
    time.sleep(3)
    login_id = driver.find_element(By.ID, "loginId--1")
    login_id.send_keys(user_id)
    time.sleep(3)
    login_pw = driver.find_element(By.ID, "password--2")
    login_pw.send_keys(pwd)
    
    # login_id = driver.find_element(By.ID, "user_email")
    # login_id.send_keys(user_id)
    
    # login_pw = driver.find_element(By.ID, "user_password")
    # login_pw.send_keys(pwd)
    
    login_id.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
# 2. 원하는 회사 리뷰 페이지까지 이동
def move_to_company(driver, company):
    search = driver.find_element(By.ID, "search_bar_search_query")
    search.send_keys(company)
    search.send_keys(Keys.RETURN)
    
    # 회사 클릭
    driver.find_element(By.CLASS_NAME, "tit").click()
    time.sleep(3)
    
    # 팝업창 없애기
    driver.find_element(By.CLASS_NAME, "btn_close_x_ty1").click()
    time.sleep(3)
    
# 3. 
if __name__ == "__main__":
    
    driver = webdriver.Chrome()
    login(driver, USER_ID, PWD)
    move_to_company(driver, QUERY)

