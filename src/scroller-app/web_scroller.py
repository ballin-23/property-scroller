# imports
from selenium import webdriver

# scroller class
class WebScroller:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def browse(self, url):
        self.driver.get(url)
        input("Press Enter to close the browser...")
        self.driver.quit()
