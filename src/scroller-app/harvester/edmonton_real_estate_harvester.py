from scrollers.web_scroller import WebScroller
from selenium import webdriver
from selenium.webdriver.common.by import By
from harvester.harvester import Harvester

# this extracts data from a web page of properties
class EdmontonRealEstateHarvester(Harvester):
    def __init__(self, driver):
        self.driver = driver
    # this assumes that you are on a page with
    def getProperties(self):
        properties_outer_container = self.driver.find_element(By.ID, "listings")
        properties_inner_container = properties_outer_container.find_element(By.CLASS_NAME, "teasers")
        anchor_tags = properties_inner_container.find_elements(By.TAG_NAME, "a")
        return anchor_tags

    
    def returnPropertyInformation(self, property):
        address = property.find_element(By.CLASS_NAME, "teaser__address")
        property_data = property.find_elements(By.CLASS_NAME, "teaser__additional-info")
        for data in property_data:
            print(data.text)
        # print(address.text)
        # print(property.get_attribute("href"))

