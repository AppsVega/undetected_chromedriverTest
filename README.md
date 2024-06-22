<h1>Automated Login Script for Stake.com</h1>
<p>This project uses Selenium with undetected_chromedriver to automate the login process for Stake.com. The script opens the Stake website, enters the username and password, and logs in automatically.</p>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>undetected_chromedriver</code> library</li>
    <li><code>selenium</code> library</li>
</ul>

<h2>Installation</h2>
<p>Install the required libraries using pip:</p>
<pre><code>pip install undetected-chromedriver selenium</code></pre>

<h2>Usage</h2>
<p>Replace <code>"seu_nome_de_usuario"</code> and <code>"sua_senha"</code> with your Stake.com username and password in the script.</p>

<h3>Running the Script</h3>
<p>To run the script, execute the following command:</p>
<pre><code>python automated_login.py</code></pre>

<h2>Code Overview</h2>
<pre><code>from undetected_chromedriver import Chrome, ChromeOptions
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

driver.quit()</code></pre>

<h2>Contributing</h2>
<p>Feel free to fork this repository and submit pull requests if you have any improvements or bug fixes.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>

<hr>
<p>Thank you for using this automated login script! If you have any questions or issues, please feel free to contact us.</p>
