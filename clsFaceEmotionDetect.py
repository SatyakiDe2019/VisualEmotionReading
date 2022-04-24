##################################################
#### Written By: SATYAKI DE                   ####
#### Written On: 17-Apr-2022                  ####
#### Modified On 20-Apr-2022                  ####
####                                          ####
#### Objective: This python class will        ####
#### track the human emotions after splitting ####
#### the audio from the video & put that      ####
#### label on top of the video frame.         ####
####                                          ####
##################################################

from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2

from clsConfig import clsConfig as cf
from deepface import DeepFace
import clsL as cl

import subprocess
import sys
import os

# Initiating Log class
l = cl.clsL()

class clsFaceEmotionDetect:
    def __init__(self):
        self.sep = str(cf.conf['SEP'])
        self.Curr_Path = str(cf.conf['INIT_PATH'])
        self.FileName = str(cf.conf['FILE_NAME'])
        self.VideoFileExtn = str(cf.conf['VIDEO_FILE_EXTN'])
        self.ImageFileExtn = str(cf.conf['IMAGE_FILE_EXTN'])

    def convert_video_to_audio_ffmpeg(self, video_file, output_ext="mp3"):
        try:
            """Converts video to audio directly using `ffmpeg` command
            with the help of subprocess module"""
            filename, ext = os.path.splitext(video_file)
            subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)

            return 0
        except Exception as e:
            x = str(e)
            print('Error: ', x)

            return 1

    def readEmotion(self, debugInd, var):
        try:
            sep = self.sep
            Curr_Path = self.Curr_Path
            FileName = self.FileName
            VideoFileExtn = self.VideoFileExtn
            ImageFileExtn = self.ImageFileExtn
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Load Video
            videoFile = Curr_Path + sep + 'Video' + sep + FileName + VideoFileExtn
            temp_path = Curr_Path + sep + 'Temp' + sep

            # Extracting the audio from the source video
            x = self.convert_video_to_audio_ffmpeg(videoFile)

            if x == 0:
                print('Successfully Audio extracted from the source file!')
            else:
                print('Failed to extract the source audio!')

            # Loading the haarcascade xml class
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # start the file video stream thread and allow the buffer to
            # start to fill
            print("[INFO] Starting video file thread...")
            fvs = FileVideoStream(videoFile).start()
            time.sleep(1.0)
            cnt = 0

            # start the FPS timer
            fps = FPS().start()

            try:
                # loop over frames from the video file stream
                while fvs.more():

                    cnt += 1
                    # grab the frame from the threaded video file stream, resize
                    # it, and convert it to grayscale (while still retaining 3
                    # channels)
                    try:
                        frame = fvs.read()
                    except Exception as e:
                        x = str(e)
                        print('Error: ', x)

                    frame = imutils.resize(frame, width=720)
                    cv2.imshow("Gonoshotru - Source", frame)

                    # Enforce Detection to False will continue the sequence even when there is no face
                    result = DeepFace.analyze(frame, enforce_detection=False, actions = ['emotion'])

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    frame = np.dstack([frame, frame, frame])

                    faces = faceCascade.detectMultiScale(image=frame, scaleFactor=1.1, minNeighbors=4, minSize=(80,80), flags=cv2.CASCADE_SCALE_IMAGE)

                    # Draw a rectangle around the face
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

                    # Use puttext method for inserting live emotion on video
                    cv2.putText(frame, result['dominant_emotion'], (50,390), font, 3, (0,0,255), 2, cv2.LINE_4)

                    # display the size of the queue on the frame
                    #cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()), (10, 30), font, 0.6, (0, 255, 0), 2)
                    cv2.imwrite(temp_path+'frame-' + str(cnt) + ImageFileExtn, frame)

                    # show the frame and update the FPS counter
                    cv2.imshow("Gonoshotru - Emotional Analysis", frame)
                    fps.update()

                    if cv2.waitKey(2) & 0xFF == ord('q'):
                        break
            except Exception as e:
                x = str(e)
                print('Error: ', x)
                print('No more frame exists!')

            # stop the timer and display FPS information
            fps.stop()
            print("[INFO] Elasped Time: {:.2f}".format(fps.elapsed()))
            print("[INFO] Approx. FPS: {:.2f}".format(fps.fps()))

            # do a bit of cleanup
            cv2.destroyAllWindows()
            fvs.stop()

            return 0

        except Exception as e:
            x = str(e)
            print('Error: ', x)

            return 1
