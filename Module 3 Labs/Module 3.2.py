# 3.2.1.3 LAB: Essentials of the while loop - Guess the secret number
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone
# who run his program to play the Guess the secret number game, and guess what number he has picked for them.
# Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
# Your task is to help the magician complete the code in the editor in such a way so that the code:
# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same as the number picked by the magician.
#the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!"
# and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen,
# and the magician should say the following words: "Well done, muggle! You are free now."
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Guess the secret number:"))
while number != 777:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Guess the secret number:"))
else:
    print("Well done, muggle! You are free now.")

#3.2.1.6 LAB: Essentials of the for loop - counting mississippily
# Your task is very simple here: write a program that uses a for loop to "count mississippily" to five.
# Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"
# For the time being, we'd just like you to know that we've imported the time module and used the sleep() 
# method to suspend the execution of each subsequent print() function inside the for loop for one second, so that the message outputted to the console resembles an actual counting. Don't worry - you'll soon learn more about modules and methods.
import time
for n in range (1,6): # Write a for loop that counts to five.
    print (n,"Mississippi") # Body of the loop - print the loop iteration number and the word "Mississippi".
    time.sleep(1) # Body of the loop - use: time.sleep(1)
print ("Ready or not, here I come!") # Write a print function with the final message.

# 3.2.1.9 LAB: The break statement - Stuck in a loop
# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word
# in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
while True:
    word = str(input("What is the word:")) # Asks to input a string
    if word == ("chupacabra"): # If the string is equal to chupacabra
        print ("You've successfully left the loop.") # Print the following output  
        break # Stop the loop.

# 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater
# Your task here is very special: you must design a vowel eater! Write a program that uses:


user_word = str(input("Enter a word: ")) # ask the user to enter a word;
user_word = user_word.upper() # use user_word = user_word.upper() to convert the word entered by the user to upper case;
for letter in user_word: #use conditional execution
    if letter == ("A"): # "eat" the following vowels A, E, I, O, U from the inputted word;
        continue
    elif letter == ("E"):
        continue
    elif letter == ("I"):
        continue
    elif letter == ("O"):
        continue
    elif letter == ("U"): 
        continue
    else:
        print (letter)

# 3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater
# Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab (3.1.2.10)
# create a better, upgraded (pretty) vowel eater! Write a program that uses:
word_without_vowels = "" # Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it
user_word = str(input("Enter a word: ")) # ask the user to enter a word;
user_word = user_word.upper() # use user_word = user_word.upper() to convert the word entered by the user to upper case;
for letter in user_word: #use conditional execution
    if letter == ("A"): # "eat" the following vowels A, E, I, O, U from the inputted word;
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter # assign the uneaten letters to the word_without_vowels variable and print the variable to the screen. 
print(word_without_vowels)

# 3.2.1.14 LAB: Essentials of the while loop
# The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
blocks = int(input("Enter the number of blocks: "))
height = 0
counter = 0
while True:
    counter += 1# Every itteration of the while loop will increment n by +1.
    blocks = blocks - counter  # Every increment in height will deduct a number of blocks from the total.
    height = height + 1 # Each itteration of the while loop will increment the height by 1.
    if blocks <= 0: 
        break
# When the appropriate ammount of blocks can not be deducted from the total, the while loop will stop.
print("The height of the pyramid:", height) 

#3.2.1.15 LAB: Collatz's hypothesis
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. 
# We also want you to count the steps needed to achieve the goal.
c0 = int(input("Input Number:")) # take any non-negative and non-zero integer number and name it c0;
counter = 0
while True:
    if c0 <= 0: # Must be a non-negative and non zero integer. This would flag up an error
        print ("Invalid Input")
        break # If a non negative or non zero value is entered it would stop the while loop
    if c0 % 2 == 0: # Is c0 a multiple of 2? I.e is it even?
        c0 = c0//2 # If it is devide it by 2
        print (c0) # print the resultant c0 after the division
        counter += 1 # add a 1 to the counter to mark the number of steps the process has been through.
    if c0 == 1: # Check to see if c0 = 0. If it is the while rule will end.
        print ("steps:", counter) # Print the word steps + the counter that is keeping track of how many iterations the cycle has been through.
        break # Stops the while rule
    if c0 % 2 != 0: # Is c0 not divisible by 2. I.e is it odd?
        c0 = 3 * c0 + 1 # If if is multiply c0 by 3 and add 1.
        print (c0) # print the resultant c0 after the equation.
        counter += 1 # add a 1 to the counter to mark the number of steps the process has been through.