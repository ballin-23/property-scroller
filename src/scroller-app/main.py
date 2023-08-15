from scrollers.edmonton_real_estate_scroller import EdmontonRealEstateScroller
import time

scroller = EdmontonRealEstateScroller()
scroller.browse("https://www.edmontonrealestate.pro/central-edmonton/downtown.php")
print("loaded")
number_of_pages = scroller.get_total_pages()
for i in range(1,number_of_pages):
    scroller.get_next_page()
    print("got page", i+1)
    time.sleep(0.5)
time.sleep(40)