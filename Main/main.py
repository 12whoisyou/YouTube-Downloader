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
    video.download()
    print(url.title+'.mp4')
    print(os.getcwd())


    print("Downloaded! :)")

def by_name():
    names = input("Enter song name and creator here: ")
    names = names.split(",")
    for count, name in enumerate(names):
        if name[0] == " ":
            name = name[1:]
            names[count] = name
        download(name)
        print(names, name)
    print(names)
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
    print(video.title+'.mp4')

    os.chdir(os.getcwd())
    os.rename(video.title+'.mp4', video.title+'.mp3')
def upload_to_phone():
    driver = webdriver.Chrome()
    driver.get("http://10.0.0.5/")
    time.sleep(10)

    for file in file_path:
        input = driver.find_element_by_id("fileupload")
        input.send_keys(os.path.abspath(file))
    driver.find_element_by_id("upload-file").click()

    time.sleep(len(file_path)*5)
    [os.remove(file) for file in file_path]

if __name__ == '__main__':
    #start()
    #by_link()
    #print(os.listdir())
    #os.rename(url.title+'.mp4', url.title+'.mp3')
    by_name()
