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
        """
        set the number of bedrooms, bathrooms, squarefootage of a property

        :param content: The first number.
        :type content: string
        """
        propertyInformation = content.split()
        if len(propertyInformation) >= 5:
            self.bedrooms = propertyInformation[0]
            self.bathrooms = propertyInformation[2]
            self.squarefootage = propertyInformation[4]
    
    def setPropertyType(self, description):
        """
        set the property type (condo, single family)

        :param description: The text from the div with the property type.
        :type description: string
        """
        if CONDO in description:
            self.propertyType = PropertyType.CONDO_TOWNHOUSE
        else:
            self.propertyType = PropertyType.SINGLE_FAMILY