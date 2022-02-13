from pytube import YouTube
from pytube import Search
import sys, os
import time

from selenium import webdriver

# I will polish the code tomrow



file_path = []
website = "http://10.0.0.5/"
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


    upload_to_phone()

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
    driver = webdriver.Chrome()
    driver.get(website)
    time.sleep(10)

    input = driver.find_element_by_id("fileupload")
    for file in file_path:
        input.send_keys(os.path.abspath(file))
    
    file_loader = driver.find_element_by_class_name("uploading")
    
    driver.find_element_by_id("upload-file").click()
    
    while file_loader.is_displayed():
        time.sleep(3)

    [os.remove(file) for file in file_path]

if __name__ == '__main__':
    print("hi and welcome to this masterpiece of a softawre")
    start()
