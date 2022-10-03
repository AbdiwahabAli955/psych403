#Create a list of numbers [1,2,3] called "numlist". Multiply the list by 2.
#Create a numpy array of numbers [1,2,3] called "numarr". Multiply the array by 2. 
#What is the difference between multiplying lists and multiplying arrays?
#Create a list of strings ['do','re','mi','fa'] called "strlist". Use operations to create the following outputs with your variable: 
import numpy as np
numlist = [1,2,3]
print(numlist *2)
numarr = np.array([1,2,3])
print(numarr*2)

strlist = ['do','re','mi','fa'] 
print([strlist[0]*2,strlist[1]*2,strlist[2]*2,strlist[3]*2])
print(strlist*2)

print([strlist[0],strlist[0],
       strlist[1],strlist[1],
       strlist[2],strlist[2],
       strlist[3],strlist[3]])

print([[strlist[0],strlist[0]],
       [strlist[1],strlist[1]],
       [strlist[2],strlist[2]],
       [strlist[3],strlist[3]]])

