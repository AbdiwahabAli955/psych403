Import exercises

    
    import numpy as np
    from psychopy import core, gui, visual, event
    import json
    import os, random, pprint


Directory exercises

1.

    image = set(os.listdir('images'))
    pics = []
    for i in range(1,11):
        if i != 10:  
            pics.append('face' + '0' + str(i) + '.jpg')
        elif i == 10:
            pics.append('face' + str(i) + '.jpg')    
            
            
    2.
     for pic in pics:
        if pic in image:
            print(pic, "was found!")
        else:  # raise an exception if the image wasn't found
            raise Exception(pic, "was not found!")

    
3.

    main_dir = os.getcwd()                                               
    data_dir = os.path.join(main_dir, 'data')                
    image_dir = os.path.join(main_dir,'imagies')            
    if not os.path.isdir(data_dir):
        raise Exception("Could not find the path!")
    if not os.path.isdir(image_dir):
        raise Exception("Could not find the path!")
        
        
 
                              
    
   
