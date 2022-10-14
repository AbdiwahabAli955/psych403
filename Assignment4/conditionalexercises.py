#Conditional exercises
#You want to tell your experiment to record participant responses. If the response is "1" or "2", print OK. If the response is "NaN" (empty), print a "subject did not respond" message. If the response is anything else, print "subject pressed the wrong key".

response1 =  input("enter response: ")
if response1 == str(1) or response == str(2):
     print('ok')
elif response1 == '':
     print('subject did not respond')
else:
     print("subject pressed the wrong key")




response2 = input('enter response: ')
if response2 == str(1):
    print('Correct')
elif response2 == str(2):
    print("incorrect")
