from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import *


class Web:
    def __init__(self):
        self.dados_site = {
            "site": "http://localhost/site/lista.html",
            "nome": "/html/body/div/div[&nome&]/div[1]",
            "preco": "/html/body/div/div[$preco$]/div[2]"
        }

        self.lista= {
            "lista_nomes": [],
            "lista_precos": []
        }

        self.driver = webdriver.Chrome()
        self.driver.minimize_window()

        self.colete_dados()
        self.pandas()


    def colete_dados(self):
        self.driver.get(self.dados_site["site"])
        try:
            for a in range(1, 11):
                nome = self.driver.find_element(By.XPATH, self.dados_site["nome"].replace('&nome&', str(a))).text
                self.lista["lista_nomes"].append(nome)
                preco = self.driver.find_element(By.XPATH,self.dados_site["preco"].replace('$preco$', str(a))).text.replace("R$", "").replace(",", ".")
                self.lista["lista_precos"].append(preco)
        finally:
            pass
        print(self.lista)

    def pandas(self):
        wb = Workbook()
        panilha = wb.active
        panilha.title = 'teste'

        aux = 1
        for item in self.lista["lista_nomes"]:
            panilha[f'A{aux}'] = item
            aux += 1

        aux = 1
        for item in self.lista["lista_precos"]:
            panilha[f'B{aux}'] = item
            aux += 1

        wb.save('teste.xlsx')

Web()

