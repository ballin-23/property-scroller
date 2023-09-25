from scrollers.edmonton_real_estate_scroller import EdmontonRealEstateScroller
from harvester.edmonton_real_estate_harvester import EdmontonRealEstateHarvester
import time
from selenium import webdriver


if __name__ == "__main__":
    driver = webdriver.Chrome()
    scroller = EdmontonRealEstateScroller(driver)
    harvester = EdmontonRealEstateHarvester(driver)
    #TODO write code to get the link of all communities
    scroller.browse("https://www.edmontonrealestate.pro/central-edmonton/downtown.php")
    print("loaded")
    number_of_pages = scroller.get_total_pages()
    for i in range(1,number_of_pages):
        propreties = harvester.getProperties()
        for property in propreties:
            try:
                harvester.returnPropertyInformation(property)
            except Exception as e:
                print(f"an error occured: {e}")

        scroller.get_next_page()
        print("got page", i+1)
        time.sleep(0.3)
    time.sleep(40)
