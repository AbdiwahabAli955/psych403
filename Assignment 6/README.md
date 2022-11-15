Dialog box exercises


    1 and 2. exp_name = 'subject info'
             exp_info = {'session':1,'subject_nr':'', 'age':'', 'handedness':('right','left','ambi'), 
                  'gender':('male','female','other','prefer not to say')}
    3 and 4. print("All variables have been created! Now ready to show the dialog box!")
             dlg = gui.DlgFromDict(dictionary=exp_info, fixed=['session'], title=exp_name,order=['session','subject_nr','handedness','gender'])
    5.       exp_name = 'subject info'
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
             
 Monitor and window exercises
     
    1. The size of the window may change if the unit is changed. Psychypy allows us to employ a variety of units. 
       The unit you choose will be determined by the devices and conditions you utilise. For example, when performing 
       the demonstration, we typically utilise the units 'norm' and 'height.' Because these units will naturally change 
       as the window size is adjusted.
    
    2. Changing the colour space alters the colour space that is currently being utilised. 
       The value should be either a string or None. If none is specified, the stimulus's default 
       colorSpace is utilised (defined during initialization). Changing the colorSpace has no effect
       on the stimulus parameters. As a result, you should normally define colorSpace before specifying the colour.
       
    3.CREATION OF WINDOW AND STIMULI
      #define the monitor settings using psychopy functions
      mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
      mon.setSizePix([2560 , 1600])
      #-define the window (size, color, units, fullscreen mode) using psychopy functions
      win = visual.Window(monitor=mon, size=(800,600), color=[-1,-1,-1])
      
Stimulus exercises¶
      
    1.image = visual.ImageStim(win, units='pix', size = (400,400))
    main_dir = os.getcwd() 
    image_dir = os.path.join(main_dir,'images')
    stimulus = ['face01.jpg','face02.jpg','face03.jpg']
    Trials=3 
    for trial in range(nTrials): 
         my_image.image = os.path.join(image_dir,stims[trial])
         my_image.draw() 
         win.flip()
         event.waitKeys()
    
     win.close()
     2.
       mon = monitors.Monitor('myMonitor', width=38.1, distance=60) 
       mon.setSizePix([2560 , 1600])
       mon.save()
       thisSize = mon.getSizePix()
       thisWidth = thisSize[0]
       thisHeight = thisSize[1]

       win = visual.Window(monitor = mon, fullscr = True)

       text = visual.TextStim(win, text = '+')
       image = visual.ImageStim(win, units='pix', size = (400,400)) 
       Trials = 4
       image_dir = os.path.join(main_dir, 'images')
       stims = ['face01.jpg', 'face02.jpg', 'face03.jpg','face04.jpg']

       horizMult = [-1, 1, 1, -1]
       verMult = [1, 1, -1, -1]

       for trial in range(Trials):
            my_image.image = os.path.join(image_dir, stims[trial])
            image.pos = (horizMult[trial] * thisWidth/4, verMult[trial] * thisHeight/4)
            image.draw()
            fix_text.draw()
            win.flip()
            event.waitKeys()

       win.close()
    
      3.
       fix_text = visual.TextStim(win, text='+')
      
      4. #CREATION OF WINDOW AND STIMULI
      #====================
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
            core.wait(.5)
        
            #-draw image
            my_image.draw()
            #-flip window
            win.flip()
            #-wait time (stimulus duration)
            core.wait(.5)
        
            #-draw end trial text
            my_text.text = end_trial_msg + str(trial) #define the text and trial #
            my_text.draw()
            #-flip window
            win.flip()
            #-wait time (stimulus duration)
            core.wait(.5)
        
        
        
    win.close()       
#=====================

