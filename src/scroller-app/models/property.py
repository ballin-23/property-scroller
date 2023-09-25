from models.constants import CONDO
from models.property_types import PropertyType

class Property:
    def __init__(self, address, price, bedrooms, bathrooms, squarefootage, propertyType):
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.squarefootage = squarefootage
        self.propertyType = propertyType
    
    def __init__(self):
        pass

    def setPropertyInformation(self, content):
        propertyInformation = content.split()
        if len(propertyInformation) >= 5:
            self.bedrooms = propertyInformation[0]
            self.bathrooms = propertyInformation[2]
            self.squarefootage = propertyInformation[4]
    
    def setPropertyType(self, description):
        print("description: ", description)
        if CONDO in description:
            self.propertyType = PropertyType.CONDO_TOWNHOUSE
        else:
            self.propertyType = PropertyType.SINGLE_FAMILY