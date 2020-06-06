from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Chrome(ChromeDriverManager().install())

# Step 1) Open Firefox 
#browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("8959443090")
password.send_keys("xxxxxxx")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Facebook"