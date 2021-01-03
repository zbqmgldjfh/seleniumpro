from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")  # 검색bar 객체 생성

search_bar.send_keys("hello!!")  # 검색대상 삽입
search_bar.send_keys(Keys.ENTER) # 대상입력이후 enter키 눌러주기 

search_results = browser.find_elements_by_class_name("g") # 검색후 list의 class element "g" 찾기 

print(search_results)

#browser.quit()  # 브라우저를 다 사용한후 닫아주기 