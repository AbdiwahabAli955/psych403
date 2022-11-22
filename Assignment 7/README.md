Wait exercises

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
    
Clock exercises

    1.
    from psychopy import visual, monitors, event, core
    mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
    mon.setSizePix([2560 , 1600])
    win = visual.Window(monitor=mon) 
    
    trial_timer = core.Clock()
    
    import os

    main_dir = os.getcwd() 
    image_dir = os.path.join(main_dir,'experiments','Imagies')

    import numpy as np 
    stims = ['face01.jpg','face02.jpg','face03.jpg'] 
    nTrials=3 
    my_image = visual.ImageStim(win,units="pix",size=(400,400))

    for trial in range(nTrials): 
        trial_timer.reset()
        core.wait(2)

        print('Trial'+str(trial)+' time =', trial_timer.getTime())
        my_image.image = os.path.join(image_dir,stims[trial])

        my_image.draw() 
        win.flip() 

    win.close()
    #results 
    Trial01 time = 2.0008399080252275
    Trial02 time = 2.0010293188970536
    Trial03 time = 2.0011532760690898
    1. It seems to be off by a few miliseconds
    
    2.
    from psychopy import visual, monitors, event, core
    from PIL import Image
    mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
    mon.setSizePix([2560 , 1600])
    win = visual.Window(monitor=mon) 

    trial_timer = core.Clock()

    import os
    os.chdir('/Desktop')
    main_dir = os.getcwd() 
    image_dir = os.path.join(main_dir,'Imagies')

    import numpy as np 
    stims = ['face01.png','face02.png','face03.png'] 
    nTrials=3 
    my_image = visual.ImageStim(win,units="pix",size=(400,400))

    trial_timer = core.Clock() 

    for trial in range(nTrials):
        trial_timer.reset()
        #-draw stimulus
        my_image.draw()
        while trial_timer.getTime()<=2:
             print('Trial'+str(trial)+' time =', trial_timer.getTime())
             my_image.image = os.path.join(image_dir,stims[trial])
             my_image.draw() 
             win.flip() 
    win.close()
    Results were not as precise as core.wait.
    
    3.
    from psychopy import visual, monitors, event, core
    from PIL import Image
    mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
    mon.setSizePix([2560 , 1600])
    win = visual.Window(monitor=mon) 
    
    trial_timer = core.Clock()

    import os
    os.chdir('/Desktop')
    main_dir = os.getcwd() 
    image_dir = os.path.join(main_dir,'Imagies')

    import numpy as np 
    stims = ['face01.png','face02.png','face03.png'] 
    nTrials=3 
    my_image = visual.ImageStim(win,units="pix",size=(400,400))

    trial_timer = core.Clock() 
    pres_timer = core.CountdownTimer() 
    for trial in range(nTrials):
        pres_timer.reset()
        pres_timer.add(2)
        my_image.draw()
        while pres_timer.getTime() >0:
            print('Trial'+str(trial)+' time =', pres_timer.getTime())
            my_image.image = os.path.join(image_dir,stims[trial])
            my_image.draw() 
            win.flip() 
    win.close()
    This was more precise than clock_wait_timer.
    
    4.
    
    from psychopy import visual, monitors, event, core, logging

    #define the monitor parameters
    mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
    mon.setSizePix([2560 , 1600])
    win = visual.Window(monitor=mon) 

    import os
    #stuff you only have to define once at the top of your script
    oos.chdir('/Desktop')
    main_dir = os.getcwd() 
    image_dir = os.path.join(main_dir,'Imagies')
    end_trial_msg = "End of trial"

    fix_text = visual.TextStim(win, text='+')
    my_image = visual.ImageStim(win)
    end_trial_text = visual.TextStim(win, text=end_trial_msg)

    stims = ['face01.jpg','face02.jpg','face03.jpg']

    nBlocks=2
    nTrials=3

    wait_timer = core.Clock()
    clock_wait_timer = core.Clock()
    countdown_timer = core.CountdownTimer()

    #=====================
    #START TRIAL
    #===================== 

    for trial in range(nTrials):
        my_image.image = os.path.join(image_dir,stims[trial])
        fix_text.draw()
        win.flip()
        core.wait(.5)
        countdown_timer.reset()
        countdown_timer.addTime(1)
        imgStartTime=wait_timer.getTime()
        while countdown_timer.getTime() > 0:
            my_image.draw()
            win.flip()

        imgEndTime = wait_timer.getTime()
        
        print("Image Duration was {} seconds".format(imgEndTime - imgStartTime))
    
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5)

    win.close()


Frame-based timing exercises

1.

    from psychopy import visual, monitors, event, core, logging

    #define the monitor parameters
    mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
    mon.setSizePix([2560 , 1600])
    win = visual.Window(monitor=mon) 

    import os
    #stuff you only have to define once at the top of your script
    oos.chdir('/Desktop')
    main_dir = os.getcwd() 
    image_dir = os.path.join(main_dir,'Imagies')

    refresh=1.0/60.0
    fix_dur = 0.2 
    image_dur = 0.1 
    text_dur = 0.2 
    
    fix_frames = int(fix_dur / refresh) #whole number
    image_frames = int(image_dur / refresh) #whole number
    text_frames = int(text_dur / refresh) #whole number
    total_frames = int(fix_frames + image_frames + text_frames)

        
    import numpy as np 
    stims = ['face01.jpg','face02.jpg','face03.jpg'] 
    nTrials=3 
    nBlocks=2
    my_image = visual.ImageStim(win,units="pix",size=(400,400))
       
    trial_timer = core.Clock() 
    block_timer = core.Clock()

    for frameN in range(total_frames):
        if 0 <= frameN <= fix_frames:
            win.flip()

            if frameN == fix_frames:
               print("End fix frame =", frameN)

        if fix_frames < frameN <= (fix_frames+image_frames):
            win.flip()
            if frameN == (fix_frames+image_frames):
                print("End image frame =", frameN)

        if (fix_frames+image_frames) < frameN < total_frames:
            win.flip()
            if frameN == (total_frames-1):
               print("End text frame =", frameN)

    win.close()
  
  
2.
  The frames did drop more then 20.
    
 
 
        
