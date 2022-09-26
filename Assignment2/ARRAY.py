import numpy as np
#Create an array called "mixnums" composed of 3 integers and 3 floats. Print the array. What has happened to the array?
#Create an array called "mixtypes" composed of 2 integers, 2 floats, and 2 strings. Print the array. What has happened to the array? What does python do to arrays with mixed types?
#Create an array called "oddarray" of all odd numbers between 0 and 100.
#Create an array called "logarray" of 16 numbers between 1 and 5 that follow a logarithmic distribution. These should not be integers.

mixnums = np.array([1,2,3,4.1,5.1,6.1])

print(mixnums)
mixtypes = np.array([1,2,3.0,4.0,"Hello","world"])
print(mixtypes)
#Create an array called "oddarray" of all odd numbers between 0 and 100.

oddarray = np.array((list(range(1,100,2))))
oddarray
print(oddarray)

oddarray2=np.arange(1,100,2)
logarray=np.logspace(1,5,16)
print(oddarray2)