Import exercises
Fill in the "Import Modules" section of the experiment structure:

    import numpy as np
    from psychopy import core, gui, visual, event
    import json
    import os, random, pprint

Directory exercises

1.

    pics = []
    counter = 0
    for i in range(10):
        counter = counter + 1
        pics.append('cat' + str(counter) + '.jpg')

2.

     for pic in pics:
        if os.path.isdir(image_dir)) == "True"
            print("cat1.jpg was found")
        if os.path.isdir(image_dir)) == "False"
            print("Image does not exist")
    
    
    
    
    
3.

    main_dir = os.getcwd()                                               
    data_dir = os.path.join(main_dir, 'data')                
    image_dir = os.path.join(main_dir,'imagies')            
    if not os.path.isdir(data_dir):
        raise Exception("Could not find the path!")
    if not os.path.isdir(image_dir):
        raise Exception("Could not find the path!")

