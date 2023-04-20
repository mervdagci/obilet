from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:
    uye_giris_btn = (By.XPATH, "//a[contains(text(),'Üye Girişi')]")
    uye_ol_btn = (By.XPATH, "//a[contains(text(),'Üye Ol')]")
    mail = (By.XPATH, "//input[@placeholder='E-posta Adresi']")
    password = (By.XPATH, "//input[@placeholder='Parola']")
    uye_ol_popup = (By.CSS_SELECTOR, "button[class='register register-button']")
    hesabim = (By.XPATH, "//a[contains(text(),'Hesabım')]")
    hesabim_email = (By.XPATH, "//input[@id='email']")
    ucak_btn = (By.XPATH, "//a[@data-event-action='Flight']")

    def __init__(self, driver, explicit_wait=45):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def clickUyeGirisi(self):
        self.wait.until(ec.element_to_be_clickable(self.uye_giris_btn)).click()

    def clickUyeOl(self):
        self.wait.until(ec.element_to_be_clickable(self.uye_ol_btn)).click()

    def clickUyeOldum(self):
        self.wait.until(ec.element_to_be_clickable(self.uye_ol_popup)).click()

    def clickHesabım(self):
        self.wait.until(ec.element_to_be_clickable(self.hesabim)).click()

    def clickUcakbtn(self):
        self.wait.until(ec.element_to_be_clickable(self.ucak_btn)).click()

    def getEmail(self):
        email = self.wait.until(ec.visibility_of_element_located(self.hesabim)).text
        return email

    def setMail(self, mail):
        eposta = self.wait.until(ec.element_to_be_clickable(self.mail))
        eposta.clear()
        eposta.send_keys(mail)

    def setPassword(self, password):
        set_password = self.wait.until(ec.element_to_be_clickable(self.password))
        set_password.clear()
        set_password.send_keys(password)
