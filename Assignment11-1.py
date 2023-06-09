"""Write a Python program that reads a text file called "input.txt" and counts the occurrences of 
each word in the file. Print the word and its count. Ignore case sensitivity 
(treat "Hello" and "hello" as the same word)."""
file_Path = "input.txt"
with open (file_Path,"r") as file:
    content=file . read()

content_lower = content.lower()
spilit_content = content_lower.split() #ignore case sensitivity
final_content = list(set(spilit_content)) #removing duplicates to make a loop with it

for i in final_content:
   print( "The number of \"", i, "\" in this file is " , spilit_content.count(i) )
    
