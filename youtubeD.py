from pytube import YouTube
import os
download_folder = "D:/D/Python_Youtube"
vid_url = input("Enter youtube video link: ")
vid_object = YouTube(vid_url)
stream = vid_object.streams.get_highest_resolution()
if stream.download(download_folder):
    print("Downloaded successfully")
    os.startfile(download_folder)