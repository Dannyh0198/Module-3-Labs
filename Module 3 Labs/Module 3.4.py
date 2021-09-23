# SSgt Daniel Hayward
# Module 3.4 Labs
# 23/09/2021

# 3.4.1.6 LAB: The basics of lists
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int (input("Input a number:"))
# Step 2: write a line of code that removes the last element from the list.
del(hat_list)[4]
# Step 3: write a line of code that prints the length of the existing list.
print (len(hat_list))

#3.4.1.13 LAB: The basics of lists - the Beatles
# step 1. create an empty list named beatles;
beatles = []
print("Step 1:", beatles)
# step 2. use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)
# step 3. use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
for i in beatles:
    i = str(input("Enter Band Member Name: ")) # Ask user to input Band member name
    if (i == "Stu Sutcliffe") or (i== "Pete Best"): # Looks at the input. If it is Stu Sutcliffe or Pete Best it moves on to the next part of the IF statement.
        beatles.append(i) # Will add either Stu Sutcliffe or Pete Best to beatles.
        print("Added to Beatles") 
        break # Stops the for loop.
    else:
        print ("Not a band member")
for i in beatles:
    i = str(input("Enter Band Member Name: ")) # Ask user to input Band member name
    if (i ==  beatles[3]): # Checks to see if the previous appendix is the same string as the current string.
        print ("Member already in Band")
        continue # Continue with the for loop.
    if (i == "Stu Sutcliffe") or (i== "Pete Best"): # Now we know the previous entry to the band. We can add the other member.
        beatles.append(i) # Will add either Stu Sutcliffe or Pete Best to beatles.
        print("Added to Beatles") 
        break # Stops the for loop.
    else:
        print ("Not a band member")
print("Step 3:", beatles)
# step 4. use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles [4] # deletes either Pete Best or Stu Sutcliffe. Which ever was added last
del beatles [3] # deletes either Pete Best or Stu Sutcliffe. Which ever was added first
print("Step 4:", beatles)
# step 5. use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert (0, "Ringo Star") # Insert the string "Ringo Star" to position 0 in the list
print("Step 5:", beatles)
# testing list legth
print("The Fab", len(beatles))

# 3.6.1.9 LAB: Operating with lists - basics
# Your task is to write a program which removes all the number repetitions from the list. 
# The goal is to have a list in which all the numbers appear not more than once.
# Hint: we encourage you to create a new list as a temporary work area - you don't need to update the list in situ.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list_without_duplicates = []
for number in my_list:  # Browse all numbers from the source list.
	if number not in list_without_duplicates:  # If the number doesn't appear within the new list...
		list_without_duplicates.append(number)  # ...append it here.
my_list = list_without_duplicates[:]  # Make a copy of new_list.
print("The list with unique elements only:")
print(my_list)