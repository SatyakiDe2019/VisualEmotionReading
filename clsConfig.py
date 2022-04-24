################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 22-Apr-2022               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### Machine-Learning & streaming dashboard.####
####                                        ####
################################################

import os
import platform as pl

class clsConfig(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'REPORT_PATH': Curr_Path + sep + 'report',
        'FILE_NAME': 'GonoshotruClimax',
        'SRC_PATH': Curr_Path + sep + 'data' + sep,
        'FINAL_PATH': Curr_Path + sep + 'Target' + sep,
        'APP_DESC_1': 'Video Emotion Capture!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'SUBDIR': 'data',
        'SEP': sep,
        'VIDEO_FILE_EXTN': '.mp4',
        'AUDIO_FILE_EXTN': '.mp3',
        'IMAGE_FILE_EXTN': '.jpg',
        'TITLE': "Gonoshotru - Emotional Analysis"
    }
