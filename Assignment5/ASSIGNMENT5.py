#=====================
#IMPORT MODULES
#=====================
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os, random, pprint
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
if not os.path.isdir(image_dir):
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
Trials = list(range(1,11))
Blocks = list(range(1,2))
#-stimulus names (and stimulus extensions, if images) *
images= ['face01', 'face02','face03', 'face4', 'face05', 'face06','face07','face08','face09','face10']
images_ext = []
for image in images:
    images_ext.append( image + '.png')

#-stimulus properties like size, orientation, location, duration *
size = 40000 #(200x200)
orientation = 
location = center
duration = 1 

startMessage = "Welcome to the experiment,please press any button to continue"
#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
conditions = list(zip(Trials, image))                                            # balanced list 


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
    random.shuffle(Trials)
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