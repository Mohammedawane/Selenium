# selenium 4

# Importer les classes nécessaires :
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Installer et gérer le pilote Chrome en utilisant ChromeDriverManager().install() :
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Accéder à l'URL spécifiée en utilisant la méthode get() de l'objet driver :
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
# Trouver l'élément ayant l'ID "....." et saisir du texte en utilisant send_keys() :
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "oxd-text--span").is_displayed()
# Maximiser la fenêtre du navigateur en utilisant la méthode maximize_window() de l'objet driver :
driver.maximize_window()

# Mettre le script en pause pendant 5 secondes en utilisant la fonction sleep() du module time :
time.sleep(5)

# Fermer la fenêtre du navigateur en utilisant la méthode close() de l'objet driver :
driver.close()
