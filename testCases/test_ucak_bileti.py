import time
from pages.login_page import LoginPage
from pages.ucak_page import Ucak
from pages.ucus_bilgileri import UcusBilgileri
from pages.dictionary_compare import DictionaryCompare


class TestUcak():
    baseURL = "https://www.obilet.com/"
    mail = "szszsdhbwed@gmail.com"
    password = "zdcsdcsdcsd"
    result = DictionaryCompare()

    def test_ucak_bileti(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Ucuz Otobüs Bileti Fiyatları, Otobüs Bileti Al - obilet.com":
            assert True
        else:
            assert False
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.clickUcakbtn()
        self.ucak = Ucak(self.driver)
        #Gidiş noktası, varış noktası, Giriş tarihi ve dönüş tarihi seçilir ve sefer aranır
        self.ucak.selectNereden()
        self.ucak.selectNereye()
        self.ucak.selectGidisTarihi()
        self.ucak.clickTekYonCheckBox()
        self.ucak.selectDonusTarihi()
        self.ucak.clickUcusAra()
        time.sleep(2)
        #Seçilen gidiş ve dönüş bilgileri karşılatırılır
        gidisDictionary=self.ucak.selectGidisUcus()
        print(gidisDictionary)

        donusDictionary=self.ucak.selectDonusUcus()
        print(donusDictionary)

        self.ub = UcusBilgileri(self.driver)

        ucakBilgiGidisDictionary=self.ub.getUcakBilgileriGidis()
        print(ucakBilgiGidisDictionary)

        ucakBilgiDonusDictionary=self.ub.getUcakBilgileriDonus()
        print(ucakBilgiDonusDictionary)

        resultGidisArray =[]
        resultDonusArray = []

        for key in gidisDictionary.keys():
            result = False

            if gidisDictionary[key] in ucakBilgiGidisDictionary.values():
                result = True
            resultGidisArray.append(result)

        for key in donusDictionary.keys():
            result = False
            if donusDictionary[key] in ucakBilgiDonusDictionary.values():
                result = True
            resultDonusArray.append(result)

        print(resultGidisArray)
        print(resultDonusArray)

        if (gidisDictionary == ucakBilgiGidisDictionary):
            print("Gidiş Bilgileiriniz Doğru.")
        else:
            print("Gidiş Bilgileiriniz Yanlış.")

        if ( donusDictionary== ucakBilgiDonusDictionary):
            print("Dönüş Bilgileiriniz Doğru.")
        else:
            print("Dönüş Bilgileiriniz Yanlış.")

        self.driver.close()
