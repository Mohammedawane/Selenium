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
driver.get("https://demo.nopcommerce.com/login?returnurl=%2F")

# Trouver l'élément ayant l'ID "....." et saisir du texte en utilisant send_keys() :
driver.find_element(By.ID, "Email").send_keys("test.test2@gmail.com")
driver.find_element(By.ID, "Password").send_keys("123458")
driver.find_element(By.CLASS_NAME, "login-button").click()

# Vérifier si l'élément est actuellement affiché à l'écran en utilisant la méthode is_displayed() :

driver.find_element(By.CLASS_NAME, "validation-summary-errors").is_displayed()

# Récupérer le contenu textuel de l'élément en utilisant la propriété 'text' :
txterror=driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
print(txterror)
# Vérifier si la chaîne de caractères "Login was unsuccessful." est présente dans la variable txterror :
assert "Login was unsuccessful." in txterror
#Ou bien:
assert txterror=="""Login was unsuccessful. Please correct the errors and try again.
No customer account found"""

# Maximiser la fenêtre du navigateur en utilisant la méthode maximize_window() de l'objet driver :
driver.maximize_window()

# Mettre le script en pause pendant 5 secondes en utilisant la fonction sleep() du module time :
time.sleep(5)

# Fermer la fenêtre du navigateur en utilisant la méthode close() de l'objet driver :
driver.close()

