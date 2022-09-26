print(1 == 1.0)
print('1'=='1.0')

print(5 == (3+2))

#Write out the statements [
#Are 1 and 1.0 equivalent?] X [Are "1" and "1.0" equivalent?] X [Are 5 and (3+2) equivalent?] 
#in proper Boolean syntax, in which you replace X with "and", "or", "and not", or "not". 
#List 5 ways to get True as your output.

print(1 == 1.0 and not ("1" == "1.0")and 5 == (3+2))
print(1 == 1.0 and not ("1" == "1.0")or 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 and  "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 or ("1" == "1.0")and 5 == (3+2))