from scrollers.web_scroller import WebScroller
from selenium import webdriver
from selenium.webdriver.common.by import By
from harvester.harvester import Harvester
from harvester.property import Property

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
        property = Property()
        address = property.find_element(By.CLASS_NAME, "teaser__address")
        property.address = address.text
        property_data = property.find_elements(By.CLASS_NAME, "teaser__additional-info")
        for i in range(len(property_data)):
            if i == 0:
                # handle the logic for storing the type of property
                pass
            else:
                # handle the logic to split text and return bedrooms, bathrooms and sqft
                pass
    
    def parsePropertyInformation(self, content, property):
        propertyInformation = content.split()
        if len(propertyInformation) >= 5:
            property.bedrooms = propertyInformation[0]
            property.bathrooms = propertyInformation[2]
            property.squarefootage = propertyInformation[4]
        return property
    
    def determinePropertyType(self, description):
        pass
            

