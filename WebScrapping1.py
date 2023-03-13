#!pip install selenium
#!pip install webdriver-manager
#!pip install html5lib

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

url = 'https://www.etf.com/etfanalytics/etf-finder'  
driver.get(url)
time.sleep(5)

button100 = driver.find_element('xpath', '''/html/body/div[5]/section/div/div[3]/
                            section/div/div/div/div/div[2]/section[2]/div[2]/section[2]/
                            div[1]/div/div[4]/button/label/span''')

driver.execute_script('arguments[0].click();', button100)

pagesNumber = driver.find_element('xpath','''/html/body/div[5]/section/div/div[3]/section/
                                div/div/div/div/div[2]/section[2]/div[2]/
                                section[2]/div[2]/div/label[2]''')
pagesNumber = int(pagesNumber.text[3:])

listTables = []
for pagina in range(0,pagesNumber):

    table = driver.find_element('xpath','''/html/body/div[5]/section/div/div[3]/section
                                /div/div/div/div/div[2]/section
                                [2]/div[2]/div/table''')
    tableHTML = table.get_attribute('outerHTML')
    tablePandas = pd.read_html(tableHTML)[0]
    listTables.append(tablePandas)

    nextPage = driver.find_element('xpath', '''/html/body/div[5]/section/div/div[3]/section/
                                    div/div/div/div/div[2]/section[2]/div[2]/section
                                    [2]/div[2]/div/span[2]''')
    
    driver.execute_script('arguments[0].click();', nextPage)

data = pd.concat(listTables)
print(data)

driver.quit()
