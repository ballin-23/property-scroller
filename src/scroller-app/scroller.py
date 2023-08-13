from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.edmontonrealestate.pro/")
# Keep the browser window open until you're ready to close it
input("Press Enter to close the browser...")
driver.quit()
