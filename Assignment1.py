# Assignment 1:-

# How do you concatenate two strings in Python?

# 1.Using the + Operator
string1="Hello,"
string2="World!"
result=string1+string2
print(result)

# 2.Using join() 
string1="Hello,"
string2="World!"
result=''.join([string1,string2])
print(result)

# 3.Using f-Strings
string1="Hello,"
string2="World!"
result=f"{string1}{string2}"
print(result)

# What method would you use to convert a string to lowercase in Python?
original_string="Hello,World!"
lowercase_string=original_string.lower() # Using lower method
print(lowercase_string)

# How can you find the length of a string in Python?
my_string="Hello, World!"
lenght=len(my_string) # Using len() function
print(lenght)

# Remove the white space from left side of given string,st="   helloLIET     ."
st="      helloLIET      ."
stripped_string=st.lstrip() # Using lstrip() method
print(stripped_string)

# What is the difference between the "insert()" and "append()" method when adding elements to a list in Python,give an example by coding.
my_list=[1,2,3]
# Append an element to the end of the list
my_list.append(4)
print("append:",my_list)

#  Insert an element at index 1 (second position) 
my_list.insert(1,90)
print("insert:",my_list)