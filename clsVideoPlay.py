###############################################
#### Updated By: SATYAKI DE                ####
#### Updated On: 17-Apr-2022               ####
####                                       ####
#### Objective: This script will play the  ####
#### video along with audio in sync.       ####
####                                       ####
###############################################

import os
import platform as pl
import cv2
import numpy as np
import glob
import re
import ffmpeg
import time
from clsConfig import clsConfig as cf
from ffpyplayer.player import MediaPlayer

import logging

os_det = pl.system()
if os_det == "Windows":
    sep = '\\'
else:
    sep = '/'

class clsVideoPlay:
    def __init__(self):
        self.fileNmFin = str(cf.conf['FILE_NAME'])
        self.final_path = str(cf.conf['FINAL_PATH'])
        self.title = str(cf.conf['TITLE'])
        self.VideoFileExtn = str(cf.conf['VIDEO_FILE_EXTN'])

    def videoP(self, file):
        try:
            cap = cv2.VideoCapture(file)
            player = MediaPlayer(file)
            start_time = time.time()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                _, val = player.get_frame(show=False)
                if val == 'eof':
                    break

                cv2.imshow(file, frame)

                elapsed = (time.time() - start_time) * 1000  # msec
                play_time = int(cap.get(cv2.CAP_PROP_POS_MSEC))
                sleep = max(1, int(play_time - elapsed))
                if cv2.waitKey(sleep) & 0xFF == ord("q"):
                    break

            player.close_player()
            cap.release()
            cv2.destroyAllWindows()

            return 0
        except Exception as e:
            x = str(e)
            print('Error: ', x)

            return 1

    def stream(self, dInd, var):
        try:
            VideoFileExtn = self.VideoFileExtn
            fileNmFin = self.fileNmFin + VideoFileExtn
            final_path = self.final_path
            title = self.title

            FullFileName = final_path + fileNmFin

            ret = self.videoP(FullFileName)

            if ret == 0:
                print('Successfully Played the Video!')

                return 0
            else:
                return 1

        except Exception as e:
            x = str(e)
            print('Error: ', x)

            return 1
