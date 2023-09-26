# imports
from abc import ABC, abstractmethod

class Harvester(ABC):
    @abstractmethod
    def getProperties(self):
        pass

    @abstractmethod
    def returnPropertyInformation(self):
        pass

    @abstractmethod
    def getCommunityLinks(self):
        pass


