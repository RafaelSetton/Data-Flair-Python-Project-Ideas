from selenium.webdriver import Chrome
from time import sleep


def download(video_id, formato, titulo):
    if formato.lower() not in ['mp3', 'mp4']:
        return 'Formato inválido'
    driver = Chrome()
    driver.get(f"https://yout.com/video/{video_id}/")
    sleep(1.5)
    if formato.lower() == 'mp4':
        driver.find_element_by_class_name(f"option-switch.switch_mp4").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[3]/div[3]/div/input").clear()
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[3]/div[3]/div/input")\
        .send_keys(titulo)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[3]/div[5]/button").click()


download("", "mp4", "Baixado com Python")
