# import screenshot
# url = "https://www.tradingview.com/chart/?symbol=BYBIT%3ABTCUSD"
# crop = "yes"
# name = "yooooowaaa.png"
# elementName = "layout__area--center"
# screenshot.snapscreen(url,crop,name,elementName)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")

# driver.get('https://www.google.com')

# Locate the search box using its name attribute value
search_box = driver.find_element('name', 'q')

search_query = 'liverpool'

# Enter the search query
search_box.send_keys(search_query)

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for a moment to let the results load
time.sleep(2)


element_class_to_click = 'Bi9oQd'  # Replace with the actual class name of the element
button_element = driver.find_element(By.CLASS_NAME, element_class_to_click)

# Perform the click action
button_element.click()
# Get the search results
# search_results = driver.find_element('h3')  # Adjust the selector based on the actual structure of the page

# Display the search results
# for result in search_results:
#     print(result.text)

# # Close the browser
# driver.quit()