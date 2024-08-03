from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

parts = []

def trechos():
    driver = webdriver.Chrome()
    driver.get('https://pt.wikipedia.org/wiki/Python')

    driver.maximize_window()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/main/header/h1')))
    name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/header/h1')
    parts.append(name.text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[2]/th/small/span/a/img')))
    logo = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[2]/th/small/span/a/img')
    logo.screenshot('logo_python.png')

    for i in range(4):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[{i+1}]')))
        p = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[{i+1}]')
        parts.append(p.text)

    driver.quit()
    return parts