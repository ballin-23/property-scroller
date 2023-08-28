from scrollers.web_scroller import WebScroller
from selenium import webdriver
from selenium.webdriver.common.by import By
from harvester.harvester import Harvester

# browses edmonton real estate website
class EdmontonRealEstateHarvester(Harvester):
    def __init__(self):
        self.driver = webdriver.Chrome()
    # this assumes that you are on a page with
    def getProperties(self):
        properties_outer_container = self.driver.find_element(By.ID, "listings")
        properties_innter_container = properties_outer_container.find_element(By.CLASS_NAME, "teasers")
        for property in properties_innter_container:
            print(property)
    
    def returnPropertyInformation(self):
        pass