# selenium 4
#Importer les classes:
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#En utilisant ChromeDriverManager().install() pour installer et gérer le pilote Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Utiliser la méthode get de l'objet driver pour accéder à l'URL spécifiée
driver.get("https://www.bdeb.qc.ca/")
#Maximiser la fenêtre du navigateur en utilisant la méthode maximize_window() de l'objet driver:
driver.maximize_window()
#Mettre le script en pause pendant 5 secondes en utilisant la fonction sleep() du module time
time.sleep(2)
#Afficher le titre de la page(récuperation dans la console):
print(driver.title)
#Afficher URL de la page:
print(driver.current_url)
#aller vers un autre site web:
driver.get("https://pypi.org/project/webdriver-manager/")
#Naviguer vers la page précédente dans l'historique du navigateur en utilisant la méthode back() de l'objet driver
driver.back()
#Naviguer vers la page suivante dans l'historique du navigateur en utilisant la méthode forward() de l'objet driver
driver.forward()
# Rafraîchir la page courante
driver.refresh()
#Récuperer le code source de la page:
# print(driver.page_source)
#Fermer le navigateur:
driver.close()