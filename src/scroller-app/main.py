from scrollers.edmonton_real_estate_scroller import EdmontonRealEstateScroller
import time

scroller = EdmontonRealEstateScroller()
scroller.browse("https://www.edmontonrealestate.pro/communities.php")
print("loaded")
neighborhoods = scroller.get_communities("zone-12-13")
for hood in neighborhoods:
    scroller.browse(hood)
    time.sleep(5)
    print(hood)