from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = "buy domain"

browser = webdriver.Chrome(ChromeDriverManager().install()) # 브라우저 열기
browser.get("https://google.com") # 주소이동 

search_bar = browser.find_element_by_class_name("gLFyf")  # class이름을 갖은 element 찾기 

search_bar.send_keys(KEYWORD)  # 검색대상 삽입
search_bar.send_keys(Keys.ENTER) # 대상입력이후 enter키 눌러주기 

search_results = browser.find_elements_by_class_name("g") # 검색후 list의 class element "g" 찾기 

for i, search_result in enumerate(search_results):
    class_name = search_result.get_attribute("class")
    if "kno-kp mnr-c g-blk" not in class_name:
        search_result.screenshot(f"screenshots/{KEYWORD}x{i}.png")

browser.quit()  # 브라우저를 다 사용한후 닫아주기 