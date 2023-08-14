from scrollers.web_scroller import WebScroller
from selenium import webdriver

# scroller class
class EdmontonRealEstateScroller(WebScroller):
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def browse(self, url):
        self.driver.get(url)
        input("Press Enter to close the browser...")
        self.driver.quit()
    
    def get_next_page(self):
        print("get next")

    def get_previous_page(self):
        print("get previous")