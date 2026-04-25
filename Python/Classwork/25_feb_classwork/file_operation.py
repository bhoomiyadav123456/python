#program to write 10 sentences given by user into a text file
#to open a file for write operation 
filev =open ("firstfile.txt","w")
#creating a blank list for storing sentence given by the user
sentence_list=[]

#------------------------------------
print("Enter any 10 sentence (hit enter key for new sentence): - first program:8")
for x in range(10):
  sentence = input()
  #appending the data into the file
  sentence_list.append(sentence)
  print("")
  print("Next Sentence - first program:14")
#------------------------
filev.writelines(sentence_list)
print("Data written successfully into the file - first program:17")
#close the file
filev.close()



'''Output:'''
Enter any 10 sentence (hit enter key for new sentence):
Hello
------------------------------
----Next Sentence----
How are you
------------------------------
----Next Sentence----
I am learning Python
------------------------------
----Next Sentence----
Python is easy
------------------------------
----Next Sentence----
I like coding
------------------------------
----Next Sentence----
This is file handling
------------------------------
----Next Sentence----
Practice daily
------------------------------
----Next Sentence----
Stay consistent
------------------------------
----Next Sentence----
Keep improving
------------------------------
----Next Sentence----
Thank you
------------------------------
----Next Sentence----
Data written successfully into the file
