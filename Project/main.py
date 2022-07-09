from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# start webdriver (opens Chrome in new window)
chrome = webdriver.Chrome()

# initialize waiter with maximum 300 seconds to wait.
waiter = WebDriverWait(chrome , 300)

# Will wait for appear of #logout element.
# I assume it shows that you are logged in.
wait.until(EC.presence_of_element_located(By.ID, "logout"))

# Extract data etc.