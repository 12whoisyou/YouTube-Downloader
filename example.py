from pytube import YouTube
url = input("Video url: > ")
yt = YouTube(url)
stream = yt.streams.first()
stream.download() # this will download in your current working Dir

#https://www.youtube.com/watch?v=rrRuBrUrnCw