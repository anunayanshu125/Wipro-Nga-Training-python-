from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()



text_input = wait.until(EC.visibility_of_element_located((By.NAME, "my-text")))
text_input.send_keys("Anunay")

password = driver.find_element(By.NAME, "my-password")
password.send_keys("test1234")

textarea = driver.find_element(By.NAME, "my-textarea")
textarea.send_keys("Learning Selenium automation")


dropdown = Select(driver.find_element(By.NAME, "my-select"))
dropdown.select_by_visible_text("Two")


checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()


radio = driver.find_element(By.ID, "my-radio-2")
radio.click()


submit = driver.find_element(By.TAG_NAME, "button")
submit.click()


message = wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
).text

print("Result:", message)

assert "received" in message.lower()

print("✅ FORM AUTOMATION SUCCESSFUL!")

driver.quit()