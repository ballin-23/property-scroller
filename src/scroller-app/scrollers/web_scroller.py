# imports
from abc import ABC, abstractmethod

class WebScroller(ABC):
    @abstractmethod
    def browse(self, url):
        pass

    @abstractmethod
    def get_next_page(self):
        pass


