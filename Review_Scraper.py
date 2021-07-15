'''
Este script extrai reviews do restaurante FAACA apenas para efeito de análise de sentimento
dos clientes em relação ao restaurante.
@micheldearaujo
'''

# Com Selenium
from selenium import webdriver
import pandas as pd
import csv
from time import sleep


path = 'C:\Program Files (x86)\chromedriver.exe'
#link = 'https://www.tripadvisor.com.br/Restaurant_Review-g304560-d12932769-Reviews-or10-Faaca_Boteco_e_Parrilla-Recife_State_of_Pernambuco.html'
link = 'https://www.tripadvisor.com.br/Restaurant_Review-g304560-d4080412-Reviews-Tio_Armenio_Shopping_rio_mar-Recife_State_of_Pernambuco.html'

def create_csv(name):
    f = open(name, 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('Review',))
    finally:
        f.close()


def get_reviews(path, link, name):

    # Abrindo o driver
    driver = webdriver.Chrome(path)
    driver.get(link)
    sleep(3)

    Warning_Button = driver.find_element_by_xpath('//*[@id="_evidon-accept-button"]')
    Warning_Button.click()
    sleep(1)

    # Vamos criar uma lista para amazenar todos os reviews
    reviews = []

    # Criando o loop entre as paginas
    paginas = 1
    try:
        while True:

            # Retorna uma lista com todos os reviews da pagina
            revs = driver.find_elements_by_class_name('partial_entry')

            # Adicionando os reviews a um arquivo CSV
            try:
                f = open(name, 'a')
                writer = csv.writer(f)
                for review in revs:
                    writer.writerow((review.text,))
                f.close()
            except:
                pass

            proximo = driver.find_element_by_xpath('//*[@id="taplc_location_reviews_list_resp_rr_resp_0"]/div/div[13]/div/div/a[2]')
            proximo.click()
            sleep(2)

            paginas += 1
    except:
        driver.quit()
        print(f'A quantidade de paginas foi {paginas}.')


create_csv('armenio.csv')
get_reviews(path, link, 'armenio.csv')