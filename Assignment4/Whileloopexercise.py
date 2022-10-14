#While loop exercises
#Create a while loop of 20 iterations that prints "image1.png" for the first 10 iterations, and "image2.png" for the next 10 iterations.
iterations = 0
while iterations < 20:
    iterations = iterations+ 1
    if iterations<= 10:
        print('image1.png')
    elif iterations <= 20:
        print('image2.png')

while iterations < 20:
    iterations = iterations+ 1
    if iterations<= 10:
        print('image1.png')
    elif iterations <= 20:
        print('image2.png')






#Create a while loop that shows an image until the participant makes a response of 1 or 2. Run it a few times to make sure it works the way you expect.

import random

#response=0
#while response != "1" and response != "2":
    #images=random.randint(0,10)
     #response = input("Enter response: ")
     #print(f'Image {str(images)}')
   
       
          
#Create a failsafe that terminates the previous while loop after 5 iterations if one of the valid responses (1,2) have not been made in that time.




response=0
max_iterations = 5
while response != "1" and response != "2" and max_iterations!= 0:
    images=random.randint(0,10)
    response = input("Enter response: ")
    print(f'Image {str(images)}')
    max_iterations -= 1