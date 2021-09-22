blocks = int(input("Enter the number of blocks: "))
height = 0
Blocks_needed_for_next_level = 0
while True:
    Blocks_needed_for_next_level += 1 # Every itteration of the while loop will increment n by +1.
    blocks = blocks - Blocks_needed_for_next_level  # Every increment in height will deduct the number of blocks needed to build the next level.
    if blocks <= 0: 
        break
    height = height + 1 # Each itteration of the while loop will increment the height by 1.
# When the appropriate ammount of blocks can not be deducted from the total, the while loop will stop.
print("The height of the pyramid:", height)    