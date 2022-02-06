from pytube import YouTube
import os
download_folder = "D:/D/Python_Youtube"
vid_url = input("Enter youtube video link: ")
vid_object = YouTube(vid_url)
stream = vid_object.streams.get_highest_resolution()
try:
    stream.download(download_folder)
    # print("Downloaded successfully")
except Exception as error:
    print("Got an error",error)

os.startfile(download_folder)

#YOUTUBE ALWAYS UPDATE SECURITY PATCHES, WITH TIME THIS WILL FAIL, WORKING AS AT DEC 2021