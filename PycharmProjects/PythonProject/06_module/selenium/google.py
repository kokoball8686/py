# 기본 설정
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip



# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)



# 구글 로그인 정보
email = ""  # 자신의 이메일 주소로 변경
password = ""        # 자신의 비밀번호로 변경


# 구글 로그인 페이지 열기
driver.get("https://accounts.google.com/")

# 이메일 입력
email_input = driver.find_element(By.ID, "identifierId")
for char in email:
    email_input.send_keys(char)
    time.sleep(0.5)  # 0.5초 대기

# 다음 버튼 클릭
next_button = driver.find_element(By.ID, "identifierNext")
next_button.click()
time.sleep(2)  # 페이지 로딩 대기

# 비밀번호 입력
password_input = driver.find_element(By.NAME, "password")
for char in password:
    password_input.send_keys(char)
    time.sleep(0.5)  # 0.5초 대기

# 다음 버튼 클릭
next_button = driver.find_element(By.ID, "passwordNext")
next_button.click()
time.sleep(5)  # 페이지 로딩 대기

# Gmail 페이지로 이동하여 최근 메일 확인
driver.get("https://mail.google.com/mail/u/0/#inbox")
time.sleep(5)  # 페이지 로딩 대기