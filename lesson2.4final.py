from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
browser = webdriver.Chrome()
import time
link = "http://suninjuly.github.io/explicit_wait2.html"

browser.get(link)

book = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_class_name("btn.btn-primary")
button.click()

import math
def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
input1=browser.find_element_by_class_name("form-control")
input1.send_keys(y)
button = browser.find_element(By.ID, 'solve')
button.click()
time.sleep(30)
browser.quit()



 