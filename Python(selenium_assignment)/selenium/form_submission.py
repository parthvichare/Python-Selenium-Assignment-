from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


form_url = 'https://forms.gle/WT68aV5UnPajeoSc8'
driver.get(form_url)


# Name Field
name_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="whsOnd zHQkBf" and @aria-labelledby="i1"]'))
)
name_field.send_keys('Parth Vichare')


# Phone NO field
phone_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="whsOnd zHQkBf" and @aria-labelledby="i5"]'))
)

# Input the phone number
phone_field.send_keys('9372597458')


#Screen Shot of First Page of form
screenshot_path = 'filled_form_screenshot1.png'
driver.save_screenshot(screenshot_path)

#Email filled
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="whsOnd zHQkBf" and @aria-labelledby="i9"]'))
)
# Input the email address
email_field.send_keys('parthuvichare9@gmail.com')


# Address Filled
address_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//textarea[@class="KHxj8b tL9Q4c" and @aria-labelledby="i13"]'))
)

# Input your address into the textarea
address_field.send_keys('Walchan Bunglow Antophill Wadala')


#Pincode filled
pincode_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="whsOnd zHQkBf" and @aria-labelledby="i17"]'))
)

# Input the pincode
pincode_field.send_keys('400037')


# DOB filled
dob_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="date" and @class="whsOnd zHQkBf" and @aria-labelledby="i25"]'))
)

dob_field.send_keys('12-09-2003') 


# Male filled
male_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="whsOnd zHQkBf" and @aria-labelledby="i26"]'))
)

# Input "Male" into the field
male_field.send_keys('Male')


#Code Filled
Code = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="whsOnd zHQkBf" and @aria-labelledby="i30"]'))
)

# Input the "By" value
Code.send_keys('GNFPYC')

screenshot_path = 'filled_form_screenshot2.png'
driver.save_screenshot(screenshot_path)

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[@class="NPEfkd RveJvd snByac" and text()="Submit"]'))
)

# Click the submit button
submit_button.click()

# Final Screenshot
screenshot_path = 'Screenshot after submission.png'
driver.save_screenshot(screenshot_path)

time.sleep(10)

driver.quit()