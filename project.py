'''
        A Gameplay Mechanic [TS4]
        By CozyGnomes (https://cozygnomes.tumblr.com/)
        This is an existing document that contains several things you can do in your gameplay on TS4. 
        This program comes with the intention of automatically generating the related phrase without 
        having to search for each number (as instructed in the original document).
        Project by Blenda C
'''
import random
FILE_NAME = 'gpmechanic.txt'

def get_mechanics():
    # read the file containing the mechanics
    list_mechanics = []
    with open(FILE_NAME, encoding='utf-8') as file:
        for line in file: # for-each loop gives lines one at a time
            list_mechanics.append(line.strip()) # strip removes whitespace at the start or end
    return list_mechanics

def introduction():
    # gives the introduction and instructions to the user
    print("")
    print("A Gameplay Mechanic [TS4] by CozyGnomes")
    print("Every time you press enter, a new suggestion for your gameplay will be generated. (to exit enter 0)")

def main():
    introduction()
    list_mechanics = get_mechanics()
    chosen_value = random.choice(list_mechanics) # comes with ‘import random’
    print("You should...")
    print('')
    print(chosen_value)
    # here is the verification if the user wants to generate an alternative mechanic or wants to leave
    while True:
        user_input = input("")
        if user_input == '':
            print("or...")
            chosen_value = random.choice(list_mechanics) 
            print(chosen_value)
        elif user_input == '0':
            break
    # once generated, a final message
    print('')
    print("Now it's time to do it! Good luck!")
    
if __name__ == '__main__':
    main()