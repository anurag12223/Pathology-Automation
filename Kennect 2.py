from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://gor-pathology.web.app/")
driver.maximize_window()
driver.implicitly_wait(10)
#login
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@kennect.io")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwerty@1234")
driver.find_element(By.XPATH, "(//div[@id='root']/div/div/form/button/span)[1]").click()
driver.implicitly_wait(10)
# time.sleep(5)

#Creating a new Patient
driver.find_element(By.XPATH,"//div[@id='root']/div/nav/div[2]/div/div/div/div[2]/ul/a[4]/div/div[2]/span").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//div[@id='root']/div/main/div[2]/div/a/button/span").click()
driver.implicitly_wait(10)
#Patient Contact Details
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Anurag1234567890")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("anurag1234567890@gmail.com")
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("9898989898")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//div[@id='root']/div/main/div[2]/div[2]/div/div[2]/div[2]/button[2]/span").click()
driver.implicitly_wait(10)

#Secondary details of Patient
driver.find_element(By.XPATH, "//input[@name='height']").send_keys("168")
driver.find_element(By.XPATH, "//input[@name='weight']").send_keys("78")
driver.find_element(By.XPATH, "//input[@name='age']").send_keys("50")
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//div[@id='mui-component-select-gender']").click()
driver.find_element(By.XPATH,"//div[@id='menu-gender']/div[3]/ul/li[2]").click()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@name='systolic']").send_keys("90")
driver.find_element(By.XPATH, "//input[@name='diastolic']").send_keys("100")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@name='diastolic']").send_keys(Keys.PAGE_DOWN)
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div[2]/div[2]/div/div[2]/div[2]/button[2]/span[1]").click()
driver.implicitly_wait(10)
#time.sleep(5)

#Test cost calculator
driver.find_element(By.XPATH,"//*[@id='root']/div/main/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/div").click()
driver.implicitly_wait(10)
button = driver.find_element(By.XPATH,"//li[@id='patient-test-option-3']/div/div")
driver.execute_script("arguments[0].click();", button)

driver.implicitly_wait(10)
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='MuiFormControl-root']//div[@role='button']").click()
driver.find_element(By.XPATH,"//div[@id='menu-']/div[3]/ul/li[3]").click()
driver.implicitly_wait(10)
time.sleep(2)


