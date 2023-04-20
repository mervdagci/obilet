import time
from pages.login_page import LoginPage
import random
import string


class TestLogin ():
    baseURL = "https://www.obilet.com/"
    password = "zdcsdcsdcsd"
    mail_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    mail = mail_name + "@gmail.com"

    def test_uye_ol(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Ucuz Otobüs Bileti Fiyatları, Otobüs Bileti Al - obilet.com":
            assert True
        else:
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.clickUyeGirisi()
        self.lp.clickUyeOl()
        time.sleep(2)
        #email oluşturup email alanına girer
        email = self.lp.setMail(self.mail)
        #password oluşturup password alanına girer
        self.lp.setPassword(self.password)
        #çıkan popupta üye ol butonuna tıklar
        self.lp.clickUyeOldum()
        #sadece login olmuş userların görebildiği hesabım sayfasına gider
        self.lp.clickHesabım()
        #mail alanından maili çeker ve üye olunan mail ile karşılatırır, aynı ise True farklı ise False döner
        email2 =self.lp.getEmail()
        if (email == email2):
            return True
        else:
            return False
        self.driver.close()
