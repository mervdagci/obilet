import time
from datetime import timedelta, date
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Ucak:
    today = date.today()
    date1 = today + timedelta(days=2)
    d1 = date1.strftime("%Y-%m-%d")
    date2 = today + timedelta(days=3)
    d2 = date2.strftime("%Y-%m-%d")

    nereden = (By.XPATH, "//input[@id='origin-input']")
    nereye = (By.XPATH, "//input[@id='destination-input']")
    gidis_tarihi = (By.XPATH, "//input[@id='departure-input']")
    gt1 = (By.CSS_SELECTOR, "[data-date='"+d1+"']")
    gt2 = (By.CSS_SELECTOR, "[data-date='"+d2+"']")

    donus_tarihi = (By.XPATH, "//input[@id='return-input']")
    ucus_ara = (By.XPATH, "//button[@id='search-button']")
    ucus_sec = (By.XPATH, "//ul[@id='outbound-journeys']")
    nereden_list = (By.XPATH, "//ob-select[@id='origin']/div[@class='results']")
    drop_nereden = (By.XPATH, "//ob-select[@id='origin']//span[@class='location'][contains(text(),'Antalya Havaliman')]")
    drop_nereye = (By.XPATH, "//ob-select[@id='destination']//span[@class='location'][contains(text(),'Ankara Esenbo')]")
    tek_yon = (By.XPATH, "//span[contains(text(),'Tek Yön')]")
    secildiMi = (By.XPATH, "//div[@id='selection']//fieldset")
    ecoFly = (By.XPATH, "//div[@class='fly-content-container EF']")
    ecoFly2 =(By.XPATH, "(//div[@class='fly-content-container EF'])[1]")


    gidis_ucus = (By.XPATH, "(//li[@class='flight flight-1 row'])[1]")
    donus_ucus = (By.XPATH, "/html[1]/body[1]/main[1]/div[8]/ul[1]/li[1]")

    gidis_saat = (By.XPATH, "//body//main[@id='main']//div[@id='selection']//div//div//div[1]//div[1]")
    gidis_varis_saat = (By.XPATH,"//ul[@class='selection-container list visible active']//div[@class='arrival']")
    gidis_havaalani = (By.XPATH, "//ul[@class='selection-container list visible active']//div[@class='left col']//span[@class='airport']")
    gidis_varis_havaalani = (By.XPATH, "//ul[@class='selection-container list visible active']//div[@class='right col']//span[@class='airport']")
    gidis_airlines = (By.XPATH, "//ul[@class='selection-container list visible active']//span[@class='name notranslate']")


    donus_saat = (By.XPATH, "//body/main[@id='main']/div[8]/ul[1]/li[1]/div[1]/ul[1]/li[1]/div[3]/div[1]/div[1]")
    donus_varis_saat = (By.XPATH, "//body/main[@id='main']/div[8]/ul[1]/li[1]/div[1]/ul[1]/li[1]/div[3]/div[3]/div[1]")
    donus_havaalani = (By.XPATH, "//ul[@id='return-journeys']/li[1]//div[@class='left col']//span[@class='airport']")
    donus_varis_havaalani = (By.XPATH, "//ul[@id='return-journeys']/li[1]//div[@class='right col']//span[@class='airport']")
    donus_airlines = (By.XPATH, "//ul[@id='return-journeys']/li[1]//span[@class='name notranslate']")

    gidisDictionary = {}
    donusDictionary = {}



    def __init__(self, driver, explicit_wait=45):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def selectNereden(self):
        self.wait.until(ec.element_to_be_clickable(self.nereden)).click()
        time.sleep(2)
        self.wait.until(ec.element_to_be_clickable(self.drop_nereden)).click()

    def selectNereye(self):
        self.wait.until(ec.element_to_be_clickable(self.nereye)).click()
        self.wait.until(ec.element_to_be_clickable(self.drop_nereye)).click()

    def selectGidisTarihi(self):
        self.wait.until(ec.element_to_be_clickable(self.gidis_tarihi)).click()
        self.wait.until(ec.visibility_of_element_located(self.gt1)).click()

    def selectDonusTarihi(self):
        self.wait.until(ec.visibility_of_element_located(self.gt2)).click()

    def clickUcusAra(self):
        self.wait.until(ec.element_to_be_clickable(self.ucus_ara)).click()

    def clickTekYonCheckBox(self):
        self.wait.until(ec.element_to_be_clickable(self.tek_yon)).click()

    def selectGidisUcus(self):
        if("Seçilen Gidiş Uçuşu" in self.driver.page_source):
            self.wait.until(ec.element_to_be_clickable(self.ecoFly)).click()
        else:
            self.wait.until(ec.element_to_be_clickable(self.gidis_ucus)).click()
        time.sleep(5)
        element = self.wait.until(ec.element_to_be_clickable(self.gidis_saat))
        inner_text_gidis_saat = self.driver.execute_script("return arguments[0].innerText;", element)
        #print(inner_text_gidis_saat)
        element = self.wait.until(ec.element_to_be_clickable(self.gidis_varis_saat))
        inner_text_varis_saat = self.driver.execute_script("return arguments[0].innerText;", element)
        #print(inner_text_varis_saat)
        element = self.wait.until(ec.element_to_be_clickable(self.gidis_havaalani))
        inner_text_gidis_havaalani = self.driver.execute_script("return arguments[0].innerText;", element)
        #print(inner_text_gidis_havaalani)
        element = self.wait.until(ec.element_to_be_clickable(self.gidis_varis_havaalani))
        inner_text_gidis_varis_havaalani = self.driver.execute_script("return arguments[0].innerText;", element)
        #print(inner_text_gidis_varis_havaalani)
        element = self.wait.until(ec.element_to_be_clickable(self.gidis_airlines))
        inner_text_gidis_airlines = self.driver.execute_script("return arguments[0].innerText;", element)
        #print(inner_text_gidis_airlines)

        self.gidisDictionary["gidis_saat"] = inner_text_gidis_saat
        self.gidisDictionary["gidis_varis_saat"] = inner_text_varis_saat
        self.gidisDictionary["gidis_havaalani"] = inner_text_gidis_havaalani
        self.gidisDictionary["gidis_varis_havaalani"] = inner_text_gidis_varis_havaalani
        self.gidisDictionary["gidis_airlines"] = inner_text_gidis_airlines

        return self.gidisDictionary

    def selectDonusUcus(self):

        time.sleep(3)
        element = self.wait.until(ec.element_to_be_clickable(self.donus_saat))
        inner_text_donus_saat = self.driver.execute_script("return arguments[0].innerText;", element)

        element = self.wait.until(ec.element_to_be_clickable(self.donus_varis_saat))
        inner_text_donus_varis_saat = self.driver.execute_script("return arguments[0].innerText;", element)

        element = self.wait.until(ec.element_to_be_clickable(self.donus_havaalani))
        inner_text_donus_havaalani = self.driver.execute_script("return arguments[0].innerText;", element)

        element = self.wait.until(ec.element_to_be_clickable(self.donus_varis_havaalani))
        inner_text_donus_varis_havaalani = self.driver.execute_script("return arguments[0].innerText;", element)

        element = self.wait.until(ec.element_to_be_clickable(self.donus_airlines))
        inner_text_donus_airlines = self.driver.execute_script("return arguments[0].innerText;", element)


        self.donusDictionary["donus_saat"] = inner_text_donus_saat
        self.donusDictionary["donus_varis_saat"] = inner_text_donus_varis_saat
        self.donusDictionary["donus_havaalani"] = inner_text_donus_havaalani
        self.donusDictionary["donus_varis_havaalani"] = inner_text_donus_varis_havaalani
        self.donusDictionary["donus_airlines"] = inner_text_donus_airlines

        time.sleep(2)
        self.wait.until(ec.element_to_be_clickable(self.donus_ucus)).click()
        time.sleep(2)
        if("Seçilen Gidiş Uçuşu" in self.driver.page_source):
            self.wait.until(ec.element_to_be_clickable(self.ecoFly2)).click()

        return self.donusDictionary
