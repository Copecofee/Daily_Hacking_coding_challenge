#!/usr/bin/python3
#
# yt_downloader.py - Download youtube videos 
#
# Made by: Copecofee | Date: 04/07/2022
# Manuntention: Copecofee Lovegood
#
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# This tool ask for the link and after that download try to base in the video's option. Finnaly when it has ended you will be able to listen the mp3 file. 
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#
# History:
#
# v1.0 07-06-2022, Copecofee:
#    - Created the Script
# v1.1 07-27-2022, Copecofee Lovegood:
#    - Adding comments
#    
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#
# The rights to: https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
# Thanks too for the blog: https://www.instagram.com/p/CetRuufFs-z/
# I just could develop part of this project thanks to analyze the exploit: https://www.exploit-db.com/exploits/50963 <- EXPLOIT Across from this I could understand and how to use the arguments in python
#
# DOCUMENATION: https://docs.python.org/3/library/argparse.html | Give at some look in the argparse's Documentation
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#
#                 .----.
#      .---------. | == |
#      |.-"""""-.| |----|
#      ||       || | == |
#      ||       || |----|
#      |'-.....-'| |::::|
#      `"")---(""` |___.|
#     /:::::::::::\" _  "
#    /:::=======:::\`\`\
#jgs `"""""""""""""`  '-'
#
#  “Intelligence is the ability to avoid doing work, yet getting the work done.” ― Linus Torvalds
#
#

#importing the modules

import argparse
import pytube
from colorama import *
from os import system as exe
import youtube_dl


# Setinng the init to don't escape the colour output
init(autoreset=True)

exe("clear")

banner = """ __   ___     ____                      _                 _           
 \ \ / / |_  |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
  \ V /| __| | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
   | | | |_  | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
   |_|  \__| |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                      """

print(Fore.GREEN+(banner))

#Defining Arguments
parser = argparse.ArgumentParser(usage="python3 yt_downloader.py -url {link to download}", description="Use to download YouTube Videos")
parser.add_argument("-url", type=str, help="The Link to download the item", required=True)
args = parser.parse_args()


#Main function
def run():
    url = args.url
    video_url = str(url)
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()
