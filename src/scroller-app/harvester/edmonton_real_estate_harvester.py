from scrollers.web_scroller import WebScroller
from selenium import webdriver
from selenium.webdriver.common.by import By
from harvester.harvester import Harvester
from harvester.property import Property
from harvester.property_types import PropertyType
from harvester.constants import CONDO, TOWNHOUSE, SINGLE_FAMILY

# this extracts data from a web page of properties
class EdmontonRealEstateHarvester(Harvester):
    def __init__(self, driver):
        self.driver = driver
    # this assumes that you are on a page with
    def getProperties(self):
        try:
            properties_outer_container = self.driver.find_element(By.ID, "listings")
            properties_inner_container = properties_outer_container.find_element(By.CLASS_NAME, "teasers")
            anchor_tags = properties_inner_container.find_elements(By.TAG_NAME, "a")
            return anchor_tags
        except Exception as e:
            print(f"an error occured: {e}")
            return []

    
    def returnPropertyInformation(self, property):
        current_property = Property()
        address = property.find_element(By.CLASS_NAME, "teaser__address")
        current_property.address = address.text
        property_data = property.find_elements(By.CLASS_NAME, "teaser__additional-info")
        for i in range(len(property_data)):
            if i == 0:
                # handle the logic for storing the type of property
                current_property.propertyType = self.getPropertyType(property_data[i].text)
            else:
                # handle the logic to split text and return bedrooms, bathrooms and sqft
                current_property = self.setPropertyInformation(property_data[i].text, current_property)
        print("bedrooms: ", current_property.bedrooms)
        print("bathrooms: ", current_property.bathrooms)
        print("address: ", current_property.address)
        print("type: ", current_property.propertyType)
        print("sqft: ", current_property.squarefootage)
    
    def setPropertyInformation(self, content, property):
        propertyInformation = content.split()
        if len(propertyInformation) >= 5:
            property.bedrooms = propertyInformation[0]
            property.bathrooms = propertyInformation[2]
            property.squarefootage = propertyInformation[4]
        return property
    
    def getPropertyType(self, description):
        if CONDO in description:
            return PropertyType.CONDO_TOWNHOUSE
        return PropertyType.SINGLE_FAMILY
            

