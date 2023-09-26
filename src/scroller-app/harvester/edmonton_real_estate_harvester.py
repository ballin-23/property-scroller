from scrollers.web_scroller import WebScroller
from selenium import webdriver
from selenium.webdriver.common.by import By
from harvester.harvester import Harvester
from models.property import Property

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
                current_property.setPropertyType(property_data[i].text)
            else:
                current_property.setPropertyInformation(property_data[i].text)
        print("bedrooms: ", current_property.bedrooms)
        print("bathrooms: ", current_property.bathrooms)
        print("address: ", current_property.address)
        print("type: ", current_property.propertyType)
        print("sqft: ", current_property.squarefootage)
        return current_property

    def getCommunityLinks(self):
        pass
            

