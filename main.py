from selenium import webdriver # 브라우저 control
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC # wait 하기 위한 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#class로 캡슐화 
class GoogleKeywordScreenshooter:

    def __init__(self, keyword, screenshots_dir): # constructor
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")  # class이름을 갖은 element 찾기 
        search_bar.send_keys(self.keyword)  # 검색대상 삽입
        search_bar.send_keys(Keys.ENTER) # 대상입력이후 enter키 눌러주기 
        try:
            # 쓰레기 요소부분 제거필수 
            waste_element = WebDriverWait(self.browser, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))
            self.browser.execute_script(
            """
                const waste = arguments[0];
                waste.parentElement.removeChild(waste)
            """,
                waste_element # arguments[0]로 들어가는 인자값 
            )
        except Exception:
            pass

        search_results = self.browser.find_elements_by_class_name("g") # 검색후 list의 class element "g" 찾기 
        for i, search_result in enumerate(search_results):
            class_name = search_result.get_attribute("class")
            if "kno-kp mnr-c g-blk" not in class_name:
                search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{i}.png")

    def finish(self):
        self.browser.quit()  # 브라우저를 다 사용한후 닫아주기 

cpp_book = GoogleKeywordScreenshooter("c++ book book", "screenshots")
cpp_book.start()
cpp_book.finish()

python_book = GoogleKeywordScreenshooter("python book", "screenshots")
python_book.start()
python_book.finish()