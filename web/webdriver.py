import time
from selenium import webdriver

# Optional argument, if not specified will search path.
# driver = webdriver.Chrome('/path/to/chromedriver')
driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml')

# Let the user actually see something!
time.sleep(5)

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

# Let the user actually see something!
time.sleep(5)

driver.quit()

# -----------------------------


# Could do it as a serice
# import time

# from selenium import webdriver
# import selenium.webdriver.chrome.service as service

# service = service.Service('/path/to/chromedriver')
# service.start()
# capabilities = {'chrome.binary': '/path/to/custom/chrome'}
# driver = webdriver.Remote(service.service_url, capabilities)
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# driver.quit()