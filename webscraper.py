from selenium import webdriver

url = 'https://www.marketwatch.com'
browser = webdriver.Firefox()
browser.get(url)

browser.find_element_by_id('ACCEPT COOKIES').click()
