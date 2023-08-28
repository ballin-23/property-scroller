from scrollers.web_scroller import WebScroller
from selenium import webdriver
from selenium.webdriver.common.by import By
from harvester.harvester import Harvester

# browses edmonton real estate website
class EdmontonRealEstateHarvester(Harvester):
    def __init__(self, driver):
        self.driver = driver
    # this assumes that you are on a page with
    def getProperties(self):
        properties_outer_container = self.driver.find_element(By.ID, "listings")
        properties_inner_container = properties_outer_container.find_element(By.CLASS_NAME, "teasers")
        anchor_tags = properties_inner_container.find_elements(By.TAG_NAME, "a")
        for anchor in anchor_tags:
            print(anchor.text)

    
    def returnPropertyInformation(self):
        pass