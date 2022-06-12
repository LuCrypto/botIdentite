from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from mail import sendMail

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

# CHROME_PATH = '/usr/bin/google-chrome'
# CHROMEDRIVER_PATH = 'C:\Program Files (x86)'
# chrome_options.binary_location = CHROME_PATH

# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
#                             chrome_options=chrome_options)

# Pour chopper n'importe quel élément, il peut attendre jusqu'à 5 secondes
driver.implicitly_wait(5)

# Ouvrir la page
driver.get("https://app.synbird.com/67300-schiltigheim-pieces-didentite-schiltigheim")

# Carte identité
nomClass = "sc-bdVaJa"
elementRoot = driver.find_element(By.CLASS_NAME, nomClass)
elementRoot.click()

# 1 personne
elementRoot = driver.find_element(By.CLASS_NAME, "sc-bwzfXH")
elementRoot.click()

# Rentrer le code du formulaire de pre demande
elementRoot = driver.find_element(By.NAME, "test")
elementRoot.send_keys("9ML8UQF5CJ")

# Valider le code
elementRoot = driver.find_element(By.CLASS_NAME, "synbird-additional-information-group")
elementRoot = elementRoot.find_element(By.CLASS_NAME, "synbird-btn")
elementRoot.click()

# Choisir la ville
elementRoot = driver.find_element(By.CLASS_NAME, "sc-bwzfXH")
elementRoot.click()

# Récupérer les dates de rdv
locationDispo = "disponibilites.png"
elementRoot = driver.find_element(By.CLASS_NAME, "synbird-timeslot-page")
elementRoot.screenshot(locationDispo)

# Table des jours
elementTable = elementRoot.find_element(By.XPATH, "//thead/tr[1]")
premierElement = elementTable.find_element(By.XPATH, "//th/div[1]")

date = premierElement.find_elements(By.CLASS_NAME, "synbird-day")
print("====================== date : ", date)

bufferString = ""
for i in range(3):
    infos = date[i].text
    print("======== infos : ", infos)
    bufferString += infos
    bufferString += '\n'

# Prévenir avec un mail
if ("juin" == date[2].text):
    print("PRENDRE UN RENDEZ VOUS !")
    # Envoie un mail avec toutes les informations
    sendMail("RENDEZ VOUS", bufferString, locationDispo)
elif ("juil" == date[2].text):
    # Envoie un mail avec toutes les informations
    sendMail("RENDEZ VOUS", bufferString, locationDispo)

# Fermer le navigateur
driver.quit()

# Permet d'enregistrer l'élément actuel dans une image
# element.screenshot("test.png")

# Ferme l'onglet actuel
# driver.close()

# Ferme le navigateur
# driver.quit()