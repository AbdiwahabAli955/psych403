Conditional exercises
 
 1.
   
    response =  input("enter response: ")
    if response == str(1) or response == str(2):
		     print('ok')
    elif response == '':
         print('subject did not respond')
    else:
         print("subject pressed the wrong key")
2.

    response = input('enter response: ')
    if response == str(1):
        print('Correct')
    elif response == str(2):
        print("incorrect")

3. Yes the script does what I expect it to do.

For loop exercises


1.  
    
		name = "Abdiwahab"
        for letters in name:
        print(letters)    

  
2.

    name = "Abdiwahab"
    count = -1
    for letters in name:
         count+= 1
         print(letters,count)
				 
				 
3.

    name_list = ["Amy","Rory", "River"]
    for names in name_list:
         print(names)
         for letters in names:
              print(letters)
							
4.

    name_list = ["Amy","Rory", "River"]
    for names in name_list:
         count = -1
         for letters in names:
              count+=1
              print(letters,count)
    
While Loop Exercises

1.

    iterations = 0
    while iterations < 20:
         iterations = iterations+ 1
         if iterations<= 10:
              print('image1.png')
         elif iterations <= 20:
              print('image2.png')
							

2.

    import random

    response=0
    while response != "1" and response != "2":
         images=random.randint(0,10)
         print(f'Image {str(images)}')
         response = input("Enter response: ")
				 
				 
3.

    response=0
    max_iterations = 5
    while response != "1" and response != "2" and max_iterations!= 0:
        images=random.randint(0,10)
        response = input("Enter response: ")
        print(f'Image {str(images)}')
        max_iterations -= 1
