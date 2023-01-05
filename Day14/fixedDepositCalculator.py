import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Day14 import excelUtils

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=ops)

driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

# driver.switch_to.alert.dismiss()

file="E:\Testing\PythonPractice\AutomationPracticeSDET\Day14\excelData.xlsx"
rows = excelUtils.getRowCount(file,"Sheet1")
print(rows)

for r in range (2,rows+1):

    #Reading data from excel
    principle = excelUtils.readData(file,"Sheet1",r,1)
    rate = excelUtils.readData(file,"Sheet1",r,2)
    per1 = excelUtils.readData(file, "Sheet1", r, 3)
    per2 = excelUtils.readData(file, "Sheet1", r, 4)
    fre = excelUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue = excelUtils.readData(file, "Sheet1", r, 6)

    #passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rate)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
    period2 = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    period2.select_by_visible_text(per2)
    frDropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frDropdown.select_by_visible_text(fre)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    actual_mvalue = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
    #Validation

    if float(exp_mvalue)==float(actual_mvalue):
        print("Test Passed")
        excelUtils.writeData(file,"Sheet1",r,8,"Passed")
        excelUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        excelUtils.writeData(file, "Sheet1", r, 8,"Failed")
        excelUtils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click() # To clear previous fields
    # time.sleep(5)

driver.close()




