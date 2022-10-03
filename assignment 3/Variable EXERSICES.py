#Variable operations exercises
#Create three variables: "sub_code", "subnr_int", and "subnr_str". 
#The sub_code should be "sub". Assign the integer 2 to subnr_int, and assign the string "2" to subnr_str. 
#Which form of subnr (int or str) can be added to sub_code to create the output "sub2"? Why don't both work?
#Use operations to create the following outputs with your variables: 
sub_code = "sub"
subnr_int = 2
subnr_str = "2"
"sub 2" 
"sub 222" 
"sub2sub2sub2" 
"subsubsub222"
print(sub_code + " "  + subnr_str ) 
print(sub_code +" "  +(subnr_str*3))
print((sub_code + subnr_str)*3)
print((sub_code*3)+(subnr_str*3))