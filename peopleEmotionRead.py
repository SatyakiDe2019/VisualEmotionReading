##################################################
#### Written By: SATYAKI DE                   ####
#### Written On: 17-Jan-2022                  ####
#### Modified On 20-Apr-2022                  ####
####                                          ####
#### Objective: This is the main calling      ####
#### python script that will invoke the       ####
#### clsFaceEmotionDetect class to initiate   ####
#### the model to read the real-time          ####
#### human emotions from video or even from   ####
#### Web-CAM & predict it continuously.       ####
##################################################

# We keep the setup code in a different class as shown below.
import clsFaceEmotionDetect as fed
import clsFrame2Video as fv
import clsVideoPlay as vp

from clsConfig import clsConfig as cf

import datetime
import logging

###############################################
###           Global Section                ###
###############################################
# Instantiating all the three classes

x1 = fed.clsFaceEmotionDetect()
x2 = fv.clsFrame2Video()
x3 = vp.clsVideoPlay()

###############################################
###    End of Global Section                ###
###############################################

def main():
    try:
        # Other useful variables
        debugInd = 'Y'
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        var1 = datetime.datetime.now()

        print('Start Time: ', str(var))
        # End of useful variables

        # Initiating Log Class
        general_log_path = str(cf.conf['LOG_PATH'])

        # Enabling Logging Info
        logging.basicConfig(filename=general_log_path + 'restoreVideo.log', level=logging.INFO)

        print('Started Capturing Real-Time Human Emotions!')

        # Execute all the pass
        r1 = x1.readEmotion(debugInd, var)
        r2 = x2.convert2Vid(debugInd, var)
        r3 = x3.stream(debugInd, var)

        if ((r1 == 0) and (r2 == 0) and (r3 == 0)):
            print('Successfully identified human emotions!')
        else:
            print('Failed to identify the human emotions!')

        var2 = datetime.datetime.now()

        c = var2 - var1
        minutes = c.total_seconds() / 60
        print('Total difference in minutes: ', str(minutes))

        print('End Time: ', str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
