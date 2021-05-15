import os
from datetime import datetime, timedelta
import time

#SELENIUM tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

url = "https://www.bmreports.com/bmrs/?q=balancing/systemsellbuyprices/historic"
start_date = "2020-09-01"
end_date = "2020-12-31"

if not os.path.exists('dataset'):
    os.makedirs('dataset')

#Starting driver
print("STARTING BROWSER...")
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd()+'/dataset')
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

driver = webdriver.Firefox(firefox_profile=fp)
wait = WebDriverWait(driver, timeout=60)

driver.get(url)

cookies = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH,'//*[@id="cc-approve-button-thissite"]'))
).click()
print("WAITING FOR RELOAD")
time.sleep(10)

#Date elements
calendar = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH,'//*[@id="edit-date-datepicker-popup-0"]'))
)
view = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH,'//*[@id="edit-clear"]'))
)

#Execute for different dates
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')

print(start_date, " TO ", end_date)

while(start_date <= end_date):
    try:
        driver.execute_script("arguments[0].value = arguments[1]", calendar, start_date.strftime('%Y-%m-%d'))
        view.click()

        wait.until(expected_conditions.invisibility_of_element_located(
            (By.XPATH,"//div[@class='blockUI blockOverlay']"))
        )

        time.sleep(5)

        download = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH,'//*[@id="-sysemsellbuyprices-historic"]/div/div[3]/div/div[4]/div[1]/a/img'))
        ).click()
    except:
        print("PROBLEM WITH: ", start_date)

    start_date += timedelta(days=1)

driver.quit()