#!/usr/bin/env python3

import urllib.request
import urllib.error
import re
import sys
import time
import os
import shlex

def video_to_audio(fileName):
    try:
        file, file_extension = os.path.splitext(fileName)
        safe_file = shlex.quote(file)  # Use shlex.quote for security
        safe_fileName = shlex.quote(fileName)
        video_to_mp3 = f'ffmpeg -i {safe_fileName} -q:a 0 -map a {safe_file}.mp3'
        os.system(video_to_mp3)
        print("Successfully converted", fileName, "into audio!")
    except OSError as err:
        print("OS error:", err)
        exit(1)

def main():
    if len(sys.argv) != 2:
        print('command usage: python3 video_to_audio.py FileName')
        exit(1)
    else:
        filePath = sys.argv[1]
        # Check if the specified file exists
        if os.path.exists(filePath):
            print("file found!")
            video_to_audio(filePath)
        else:
            print("File not found.")
            exit(1)

# Install ffmpeg if you get an error saying that the program is currently not installed
if __name__ == '__main__':
    main()
