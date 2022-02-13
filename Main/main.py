from pytube import YouTube
from pytube import Search
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# I will polish the code tomrow



file_path = []

os.chdir(os.getcwd())

def start():
    names = input("Enter song name and creator here: ")
    
    names = names.split(",")
    for count, name in enumerate(names):
        if name[0] == " ":
            name = name[1:]
            names[count] = name
        download(name)
        print("downloaded: "+name)
        
    print("Downloaded all files")

    try: 
        upload_to_phone()
    except:
        print("your phone is not hosting the website")
        print("or you interenett is slow")
        time.sleep(2.0)

def download(name):
    if "https" in name:
        video = YouTube(name) 
    else: 
        s = Search(name+ " audio")
        video = s.results[0]

    video = video.streams.filter(only_audio=True).first()
    file_path.append(video.title+'.mp3')
    video.download(filename=video.title+'.mp4')
    os.rename(video.title+'.mp4', video.title+'.mp3')


def upload_to_phone():
    print("Make sure that your phone is on")
    print("Example website is http://10.0.0.5")

    website = input("Which website is your phone telling to upload on? ")
    driver = webdriver.Chrome()
    driver.get(website)

    #Making sure it's loaded
    time.sleep(5)

    input_web = driver.find_element(By.ID, "fileupload")
    
    for count, file in enumerate(file_path):
        file_path[count] = os.path.abspath(file)
        
    input_web.send_keys(os.path.abspath(" \n ".join(file_path)))


    file_loader = driver.find_element(By.CLASS_NAME, "uploading")
    
    driver.find_element(By.ID, "upload-file").click()
    
    while file_loader.is_displayed():
        time.sleep(3)

    [os.remove(file) for file in file_path]

if __name__ == '__main__':
    print("hi and welcome to this masterpiece of a softawre")
    start()

