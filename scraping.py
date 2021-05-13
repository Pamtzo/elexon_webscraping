import os

#SELENIUM tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

url = "https://www.bmreports.com/bmrs/?q=balancing/systemsellbuyprices/historic"

#Starting driver
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

driver = webdriver.Firefox(firefox_profile=fp)
wait = WebDriverWait(driver, timeout=5)

driver.get(url)

cookies = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH,'//*[@id="cc-approve-button-thissite"]'))
).click()

#Date elements
calendar = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH,'//*[@id="edit-date-datepicker-popup-0"]'))
)
view = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH,'//*[@id="edit-clear"]'))
)

#Execute for different dates
driver.execute_script("arguments[0].value = arguments[1]", calendar, "2020-12-03")
view.click()

wait.until(expected_conditions.invisibility_of_element_located(
    (By.XPATH,"//div[@class='blockUI blockOverlay']"))
)
download = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH,'//*[@id="-sysemsellbuyprices-historic"]/div/div[3]/div/div[4]/div[1]/a/img'))
).click()

driver.quit()