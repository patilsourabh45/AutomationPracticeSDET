from selenium import webdriver


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service(r"C:\Users\Sourabh Patil\AppData\Local\Programs\Python\Python310\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


driver = headless_chrome()
driver.get("https://admin-demo.nopcommerce.com/")
print(driver.title)
