import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")
elem = driver.find_element_by_name("search_query")
elem.clear()
elem.send_keys("Cocomelon")
elem.send_keys(Keys.RETURN)
elx = driver.find_element_by_id("mouseover-overlay")
elx.click()
assert "No results found." not in driver.page_source
