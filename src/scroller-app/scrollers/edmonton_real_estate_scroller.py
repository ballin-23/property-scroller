from scrollers.web_scroller import WebScroller
from selenium import webdriver
from selenium.webdriver.common.by import By

# browses edmonton real estate website
class EdmontonRealEstateScroller(WebScroller):
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def browse(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def get_next_page(self):
        next_button = self.driver.find_element(By.XPATH, "//a[@title='Next Page']").click()
    
    def get_previous_page(self):
        return super().get_previous_page()()
    
    def get_pages(self):
        pagination = self.driver.find_element(By.CLASS_NAME, "pagination")
        anchor_tags = pagination.find_elements(By.TAG_NAME, "a")
        page_numbers = []
        for anchor_tag in anchor_tags:
            if len(anchor_tag.text) <= 3:
                page_numbers.append(int(anchor_tag.text))
        return max(page_numbers)
    
    def has_next_page(self):
        try:
            next_button = self.driver.find_elements(By.XPATH, "//a[@title='Next Page']")
            if len(next_button) > 1:
                return True
        except:
            return False
    
    def get_communities(self, zone):
        list_links = []
        communities = self.driver.find_elements(By.CLASS_NAME, "communities-nav")
        for community in communities:
            searched_zone = community.find_elements(By.ID, zone)
            if len(searched_zone) > 0:
                communities_in_zone = community.find_element(By.CLASS_NAME, "nav").find_elements(By.TAG_NAME, 'a')
                for anchor in communities_in_zone:
                    list_links.append(anchor.get_attribute('href'))
        return list_links