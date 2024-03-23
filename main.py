from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

options = ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = Chrome(options=options)

# Abre o site da Stake
driver.get("https://stake.com/pt?tab=login&modal=auth")

time.sleep(3)

username_input = driver.find_element(By.XPATH, '//*[@id="svelte"]/div[1]/div[2]/div/div/div[2]/form/label[1]/div/div[1]/input')
username_input.send_keys("seu_nome_de_usuario")

password_input = driver.find_element(By.XPATH, '//*[@id="svelte"]/div[1]/div[2]/div/div/div[2]/form/label[2]/div/div[1]/input')
password_input.send_keys("sua_senha")

login_button = driver.find_element(By.XPATH, '//*[@id="svelte"]/div[1]/div[2]/div/div/div[2]/form/button')
login_button.click()

time.sleep(5)

driver.quit()