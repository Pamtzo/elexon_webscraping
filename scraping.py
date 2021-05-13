from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

url = "https://www.bmreports.com/bmrs/?q=balancing/systemsellbuyprices/historic"
tittle = "System Sell & System Buy Prices"

driver = webdriver.Firefox()
wait = WebDriverWait(driver, timeout=3)

driver.get(url)
wait.until(expected_conditions.title_contains(tittle))

calendar = driver.find_element_by_xpath('//*[@id="edit-date-datepicker-popup-0"]')
view = driver.find_element_by_xpath('//*[@id="edit-clear"]')

driver.execute_script("arguments[0].value = arguments[1]", calendar, "2020-12-03")
view.click()