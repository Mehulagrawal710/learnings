import pandas as pd
import time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome("C://Users//DELL//Downloads//chromedriver_win32//chromedriver.exe")

def recent_posts(username):
	url = "https://www.instagram.com/"+username+"/"
	driver.get(url)
	post = "https://www.instagram.com/p/"
	post_links = []
	while len(post_links)<25:
		links = [a.get_attribute('href') for a in driver.find_elements_by_tag_name('a')]
		for link in links:
			if post in link and link not in post_links:
				post_links.append(link)
		scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
		driver.execute_script(scroll_down)
		time.sleep(10)
	else:
		return post_links[:25]

sneakers_urls = recent_posts('sneakersthecorgi')
print(sneakers_urls)
driver.close()