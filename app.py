import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome("/Users/smrutilagnachoudhury/PycharmProjects/HelloWorld/venv/bin/chromedriver")
driver.get("https://learn-staging.byjus.com")
time.sleep(5)
print(driver.title)
driver.find_element(By.CLASS_NAME, 'MuiButton-label').click()
time.sleep(4)

user_no = driver.find_element(By.ID, 'enterNumber')
user_no.send_keys(9148708821)
time.sleep(6)

next_button1 = driver.find_element_by_class_name('nextButtonLanding')
next_button1.click()
time.sleep(5)

user_pwd = driver.find_element(By.ID, 'enterPassNumber')
user_pwd.send_keys('Strawberry123')
time.sleep(6)


#enter_otp = driver.find_element_by_id('enterPassNumber')
#enter_otp.send_keys(1111)
#time.sleep(5)

#user_name = driver.find_element_by_id('name')
#user_name.send_keys('Strawberry')
#time.sleep(5)
#user_email = driver.find_element_by_id('email')
#user_email.send_keys('Strawberry@gmail.com')
#time.sleep(10)
#user_loc= driver.find_element_by_id('txtSearchValue')
#user_loc.send_keys('Bangalore')
#time.sleep(10)
#user_loc1 = driver.find_element_by_class_name('option')
#user_loc1.send_keys('Bangalore')
#time.sleep(10)
#user_grade = driver.find_element_by_id('grade')
#user_grade.send_keys('8th Grade')
#time.sleep(5)
#next_button3 = driver.find_element_by_class_name('nextButton')
#next_button3.click()


time.sleep(6)

next_button2 = driver.find_element_by_class_name('nextButtonLanding')
next_button2.click()
time.sleep(5)


#driver.close()