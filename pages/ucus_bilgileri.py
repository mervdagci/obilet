import time
from datetime import timedelta, date
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class UcusBilgileri:
    gidis_saat = (By.XPATH, "//table[@class='journey']/tbody[1]//td[@class='departure']")
    gidis_varıs_saat = (By.XPATH, "//table[@class='journey']/tbody[1]//td[@class='arrival']")
    gidis_havaalani = (By.XPATH, "//table[@class='journey']/tbody[1]//td[@class='departure']")
    gidis_varis_havaalani = (By.XPATH, "//table[@class='journey']/tbody[1]//td[@class='arrival']")
    gidis_airlines = (By.XPATH, "//table[@class='journey']/tbody[1]//div[@class='partner-info']")

    donus_saat = (By.XPATH, "//tr[3]//td[@class='departure']")
    donus_varıs_saat = (By.XPATH, "//tr[3]//td[@class='arrival']")
    donus_havaalani = (By.XPATH, "//tr[3]//td[@class='departure']")
    donus_varis_havaalani = (By.XPATH, "//tr[3]//td[@class='arrival']")
    donus_airlines = (By.XPATH, "//tr[3]//div[@class='partner-info']")

    gidisDictionary = {}
    donusDictionary = {}

    def __init__(self, driver, explicit_wait=45):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def getUcakBilgileriGidis(self):
        element = self.wait.until(ec.element_to_be_clickable(self.gidis_saat))
        inner_text_gidis_saat = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[1]

        element = self.wait.until(ec.element_to_be_clickable(self.gidis_varıs_saat))
        inner_text_varis_saat = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[1]

        element = self.wait.until(ec.element_to_be_clickable(self.gidis_havaalani))
        inner_text_gidis_havaalani = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[0]

        element = self.wait.until(ec.element_to_be_clickable(self.gidis_varis_havaalani))
        inner_text_gidis_varis_havaalani = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[0]

        element = self.wait.until(ec.element_to_be_clickable(self.gidis_airlines))
        inner_text_gidis_airlines = self.driver.execute_script("return arguments[0].innerText;", element).split(' -')[0]

        self.gidisDictionary["gidis_saat"] = inner_text_gidis_saat
        self.gidisDictionary["gidis_varis_saat"] = inner_text_varis_saat
        self.gidisDictionary["gidis_havaalani"] = inner_text_gidis_havaalani
        self.gidisDictionary["gidis_varis_havaalani"] = inner_text_gidis_varis_havaalani
        self.gidisDictionary["gidis_airlines"] = inner_text_gidis_airlines

        return self.gidisDictionary


    def getUcakBilgileriDonus(self):
        element = self.wait.until(ec.element_to_be_clickable(self.donus_saat))
        inner_text_donus_saat = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[1]
        #print(inner_text_donus_saat)
        element = self.wait.until(ec.element_to_be_clickable(self.donus_varıs_saat))
        inner_text_donus_varis_saat = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[1]
        #print(inner_text_donus_varis_saat)
        element = self.wait.until(ec.element_to_be_clickable(self.donus_havaalani))
        inner_text_donus_havaalani = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[0]
        #print(inner_text_donus_havaalani)
        element = self.wait.until(ec.element_to_be_clickable(self.donus_varis_havaalani))
        inner_text_donus_varis_havaalani = self.driver.execute_script("return arguments[0].innerText;", element).split(' ')[0]
        #print(inner_text_donus_varis_havaalani)
        element = self.wait.until(ec.element_to_be_clickable(self.donus_airlines))
        inner_text_donus_airlines = self.driver.execute_script("return arguments[0].innerText;", element).split(' -')[0]
        #print(inner_text_donus_airlines)

        self.donusDictionary["donus_saat"] = inner_text_donus_saat
        self.donusDictionary["donus_varis_saat"] = inner_text_donus_varis_saat
        self.donusDictionary["donus_havaalani"] = inner_text_donus_havaalani
        self.donusDictionary["donus_varis_havaalani"] = inner_text_donus_varis_havaalani
        self.donusDictionary["donus_airlines"] = inner_text_donus_airlines

        return self.donusDictionary


