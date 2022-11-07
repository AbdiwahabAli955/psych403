#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, gui, visual, event,data,monitors
import json
import os
import random
from datetime import datetime


#=====================
#PATH SETTINGS
#=====================
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'experiments','data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'experiments','imagies')

#-check that these directories exist
print(os.path.isdir(data_dir))
print(os.path.isdir(image_dir))
#=====================
#COLLECT PARTICIPANT INFO
#=====================
exp_name = 'subject info'
exp_info = {'session':1,'subject_nr':'', 'age':'', 'handedness':('right','left','ambi'), 
            'gender':('male','female','other','prefer not to say')}

print ("All variables have been created! Now ready to show the dialog box!")           
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name,order=['session','subject_nr','handedness','gender'])

#get date and time
date = datetime.now()
exp_info['date'] = str(date.day) +'/'+ str(date.month) +'/'+ str(date.year)
#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
sub_dir = os.path.join(main_dir,'sub_info',filename)


#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
Trials = list(range(1,11))
Blocks = 2
#-stimulus names (and stimulus extensions, if images) *
stimulus_name = "face"
stimulus_extension='.jpg'
#-stimulus properties like size, orientation, location, duration *
size = (200,200)
orientation = "landscape"
duration = 1
location =[0,0]

#-start message text *
start_msg = "Welcome to my experiment!"
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
pics = []
for index in range(1,11):
    if index < 10:
        pics.append(stimulus_name + "0" + str(index) + stimulus_extension)
    else:
        pics.append(stimulus_name + str(index) + stimulus_extension)
for pic in pics:
    if pic in os.listdir(image_dir):
        print(pic + " was found!")
    else:
        raise Exception("The image lists do not match up!")

#-create counterbalanced list of all conditions *
conditions = list(zip(pics,trials))

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is  #correct") *
CR= []
#-create an empty list for participant responses (e.g., "on this trial, response was a  #X") *
PR =[]
#-create an empty list for response accuracy collection (e.g., "was participant #correct?") *
RAC =[]
#-create an empty list for response time collection *
RT =[]
#-create an empty list for recording the order of stimulus identities *
S_ID = []
#-create an empty list for recording the order of stimulus properties *
S_PR=[]
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
mon.setSizePix([2560 , 1600])
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(800,600), color=[-1,-1,-1])
#-define experiment start text unsing psychopy function
my_text = visual.TextStim(win, text=start_msg)
#-define block (start)/end text using psychopy functions
my_text.draw()
win.flip()
event.waitKeys()
win.close() 
#-define stimuli using psychopy functions
my_text = visual.TextStim(win) #create the text stimulus but don't define the text yet
my_text.text = start_msg #define the text
my_text.text = block_msg #define the text
my_text.text = end_trial_msg #define the text
#-create response time clock

#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press
my_text.text = start_msg #define the text
my_text.draw()
my_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys() #wait for keypress


#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
    #-present block start message
    #-randomize order of trials here *
    #-reset response time clock here
for block in range(Blocks):
    my_text.text = block_msg #define the text
    np.random.shuffle(pics)
    my_text.draw()
    win.flip()
    event.waitKeys()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
    for trial in range(Trials):
        my_image = visual.ImageStim(win)
        my_image.image = os.path.join(image_dir,stims[trial])
       #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw end trial text
        my_text.text = end_trial_msg + str(trial) #define the text and trial #
        my_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys() 
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
        
    win.close()       
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment
