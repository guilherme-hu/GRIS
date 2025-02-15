from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = f"http://challs.grisufrj.com:5004/login"
driver.get(url)

# Encontra o campo de username e escreve "oi"
username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
username_field.send_keys("oi")

# Encontra o campo de password e escreve "oi"
password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
password_field.send_keys("oi")

# Envia o formulário
login_button = driver.find_element(By.XPATH, '//*[@id="login"]')
login_button.click()

time.sleep(5)  # Espera 5 segundos para carregar a página 

# Itera de 2 a 500
for i in range(2, 501):
    url = f"http://challs.grisufrj.com:5004/notes/{i}"
    driver.get(url)
    time.sleep(1)  # Espera 1 segundo para carregar a página 
    
    # Captura o texto dentro do container <p>
    try:
        paragraph = driver.find_element(By.TAG_NAME, "p")
        if paragraph.text != "Nada aqui!":
            print(f"URL: {url} - Text: {paragraph.text}")
    except:
        print(f"URL: {url} - No <p> tag found")

# Fecha o navegador
driver.quit()