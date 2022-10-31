#=====================
#IMPORT MODULES
#=====================
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os
#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()                                                          
#-define the directory where you will save your data
data_dir = os.path.join(main_dir, 'data')                
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'imagies')            
#-check that these directories exist
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
Trials = 10
Blocks = 2
#-stimulus names (and stimulus extensions, if images) *
cats = ['faces'] * 10
images = ['image01.png', 'image02.png', 'image03.png', 'image04.png', 'image05.png', 'image06.png', 'image7.png', 'image8.png', 'image9.png', 'image10.png']

#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200]
stimOrient = 
stimLoc = [0,0]
stimDur = 1

startMessage = "Welcome to the experiment,please press any button to continue"
#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
image = set(os.listdir('images'))
pics = []
for i in range(1,11):
    if i != 10:  
        pics.append('face' + '0' + str(i) + '.jpg')
    elif i == 10:
            pics.append('face' + str(i) + '.jpg')

for pic in pics:
    if pic in image:
      print(pic, "was found!")
    else:  # raise an exception if the image wasn't found
      raise Exception(pic, "was not found!")

#-create counterbalanced list of all conditions *
conditions = list(zip(cats, images))                                            # balanced list 


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
correct_response = []
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
participant_response=[]
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
accuracy_list = []
#-create an empty list for response time collection *
rt = []
#-create an empty list for recording the order of stimulus identities *
record_ord_id= []
#-create an empty list for recording the order of stimulus properties *
record_ord_prp=[]


#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(Blocks):

    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(conditions)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(Trials):

        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment
