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

# 웹페이지 해당 주소 이동
driver.get('https://nid.naver.com/nidlogin.login')


# 네이버 로그인 정보
NAVER_ID = ''  # 네이버 ID 입력
NAVER_PASSWORD = ''  # 네이버 비밀번호 입력


# 로그인
time.sleep(2)  # 페이지 로딩 대기
driver.find_element(By.ID, 'id').send_keys(NAVER_ID)
driver.find_element(By.ID, 'pw').send_keys(NAVER_PASSWORD)
driver.find_element(By.ID, 'pw').send_keys(Keys.RETURN)


# 메일 페이지로 이동
time.sleep(30)  # 로그인 후 대기

driver.get('https://mail.naver.com/')

# 메일 목록 로딩 대기
time.sleep(3)

# 가장 최근 메일 확인
recent_mail = driver.find_element(By.CSS_SELECTOR, 'div.mail_list > ul > li:first-child')
recent_mail_title = recent_mail.find_element(By.CSS_SELECTOR, 'a.subject').text
recent_mail_sender = recent_mail.find_element(By.CSS_SELECTOR, 'span.sender').text