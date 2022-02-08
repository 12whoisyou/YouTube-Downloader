from pytube import YouTube
from pytube import Search
import os
import time

from selenium import webdriver


file_path = []
def start():
    print("hello, welcome to Music Downloader 1000")
    prefred_type = input("Would you like to download music by link or name? ")

    if prefred_type == "name":
        by_name()
    elif prefred_type == "link":
        by_link()
    else:
        start()


def by_link():
    link = input("Enter link here: ")

    url = YouTube(link)
    print(url.title)
    print("downloading....")

    video = url.streams.filter(only_audio=True).first()
    

    #path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
    #video.download(path_to_download_folder, filename=url.title+'.mp3')
    os.chdir(os.getcwd())
    video.download()
    print(url.title+'.mp4')
    print(os.getcwd())
    os.rename(url.title+'.mp4', url.title+'.mp3')

    print("Downloaded! :)")

def by_name():
    names = input("Enter song name and creator here: ")
    names = names.split(",")
    
    for name in names:
        download_by_search(name)
    
    print("Downloaded all files")

    upload_to_phone()

def download_by_search(name):
    s = Search(name+ " audio")
    while len(s.results) == 0:
        print("Has to wait extra")
    first_video = s.results[0]
    #first_video = first_video.streams.filter(only_audio=True).first()
    file_path.append(first_video.title+'.mp4')
    first_video.download(filename=first_video.title+'.mp4')
    print(first_video.title+'.mp4')

def upload_to_phone():
    driver = webdriver.Chrome()
    driver.get("http://10.0.0.7/")
    
    for file in file_path:
        input = driver.find_element_by_id("fileupload")
        input.send_keys(os.path.abspath(file))

    driver.find_element_by_id("upload-file").click()

    time.sleep(20)


if __name__ == '__main__':
    #start()
    #by_link()
    print(os.listdir())
    #os.rename(url.title+'.mp4', url.title+'.mp3')