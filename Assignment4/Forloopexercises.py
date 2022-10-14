#Remember the exercise where you printed each letter of your name? Create a for loop that prints each letter without writing out all of the print statements manually.
name = "Abdiwahab"
for letters in name:
    print(letters)
#Add an index counter and modify your loop to print the index number after each letter
name = "Abdiwahab"
count = -1
for letters in name:
    count+= 1
    print(letters,count)
    

#Create a list of names "Amy","Rory", and "River". Create a nested for loop to loop through each letter of each name.
name_list = ["Amy","Rory", "River"]
for names in name_list:
     print(names)
     for letters in names:
          print(letters)







#Add an index counter that gives the index of each letter for each name. The counter should start over at 0 for each name in the list.
name_list = ["Amy","Rory", "River"]
for names in name_list:
     count = -1
     for letters in names:
          count+=1
          print(letters,count)
          
While loop exercises