from pytube import YouTube
from pytube import Search
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



#Fully working. It throughs some error which annys me
#Any idea on how to get rid of them?

file_path = [] #Storing file name until making them to full path

os.chdir(os.getcwd()) #Making sure the os opreates in the current dir

def start():
    #Getting the names
    names = input("Enter song name and creator here: ")
    names = names.split(",")

    #Downloading the music
    try:
        for count, name in enumerate(names):
            if name[0] == " ":
                name = name[1:]
                names[count] = name
            download(name)
            print("downloaded: "+name)
        print("Downloaded all files")
    except:
        throw_error("Could not download all files")
    
    #Uploading the music
    try: 
        upload_to_phone()
    except:
        throw_error("Phone is not on or your internet is not on")

def download(name):
    #By link or by search?
    if "https" in name:
        video = YouTube(name) 
    else: 
        s = Search(name+ " full audio")
        video = s.results[0]

    #Downloading the video as audio
    video = video.streams.filter(only_audio=True).first()
    file_path.append(video.title+'.mp3')
    video.download(filename=video.title+'.mp4')

    #From mp4 to mp3
    os.rename(video.title+'.mp4', video.title+'.mp3')


def upload_to_phone():
    #Getting the website
    print("Make sure that your phone is on")
    print("Example website is http://10.0.0.5")
    website = input("Which website is your phone telling to upload on? ")
    driver = webdriver.Chrome(os.path.abspath("chromedriver.exe"))
    driver.get(website)


    #Uploading files to the website
    input_web = driver.find_element(By.ID, "fileupload")
    for count, file in enumerate(file_path):
        file_path[count] = os.path.abspath(file)
    input_web.send_keys(" \n ".join(file_path))

    #Making sure everything is uploaded and ending the program
    file_loader = driver.find_element(By.CLASS_NAME, "uploading")
    driver.find_element(By.ID, "upload-file").click()
    while file_loader.is_displayed():
        time.sleep(3)
    throw_error("Everything is uploaded, Thanks for usign my app!")

def delete_files():
    [os.remove(file) for file in file_path]

def throw_error(err_message): #This is also used to when the program has done it's job
    print(err_message)    
    time.sleep(2)
    delete_files()
    quit()

if __name__ == '__main__':
    start()


