PsychoPy keypress exercises


    1.
    from psychopy import event, visual, monitors
    from psychopy import core

    mon = monitors.Monitor('myMonitor', width=33.782, distance=60)
    mon.setSizePix([2560 , 1600])
    win = visual.Window(monitor=mon)

    nTrials = 1

    for trial in range(nTrials):
        core.wait(2)
        keys=event.getKeys()
        if keys:
           sub_resp = keys[0] 
        print("the first response is", sub_resp)
    win.close()
    
    
    
    2. 
      - Changing the position of the code can change how we collect the number. If we put the event.ClearEvents 
        within the trail loop it will reset the number of pressed keys for each trail.
  
      - If we change the position of event.ClearEvents to outside the trial loop, the keys will be cleared every time 
        we press them.
  
      - It will run through the entire 2 seconds and count the total number of keys pressed in only 2 seconds 
        instead of all trials if we remove the indentation from the "if keys:" statement.
        


Recording data exercisesÂ¶
- Answer in recording_data.py
    
    
Save csv exercisesÂ¶
- answer in assignment8.py file
- csv answer in subject1session1 file


Read JSON exercises



<img width="576" alt="Screen Shot 2022-11-28 at 5 36 47 PM" src="https://user-images.githubusercontent.com/113719490/204409825-5b7b420f-18b8-4f51-8200-4622c728b856.png">



read assignment8.py file

    

