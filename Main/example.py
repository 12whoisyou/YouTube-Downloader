import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

file_path = ['Drake - Money In The Grave (Audio) ft. Rick Ross.mp3', 'Chief Keef - Love Sosa.mp3']

def upload_to_phone():
    driver = webdriver.Chrome()
    driver.get("http://10.0.0.5/")
    time.sleep(5)
    input_web = driver.find_element(By.ID, "fileupload")
    
    for count, file in enumerate(file_path):
        file_path[count] = os.path.abspath(file)
        

    input_web.send_keys(os.path.abspath(" \n ".join(file_path)))


    file_loader = driver.find_element(By.CLASS_NAME, "uploading")
    
    driver.find_element(By.ID, "upload-file").click()
    
    while file_loader.is_displayed():
        time.sleep(3)

upload_to_phone()