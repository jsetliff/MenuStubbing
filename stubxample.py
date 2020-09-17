"""
File Name: stubxample.py
Function List:
    PrintMenu       Used to more easily display menu
    Clear           Used to clear the terminal, uses os.system and
                    and os.name to ensure proper system call
    MenuSelection   Used to "switch" on the user menu choice
    MenuOne -
        MenuTen     Stubbed functions. Functionality TBD.
    WaitForEnter    Displays interactivity message and uses throwaway
                    input() to require a Return to proceed
"""

from os import system, name

"""
Function: PrintMenu()   Prints menu to terminal
Input Variables: none
Output Variables: none
Global Variables: none

Version History:
    08/16/2020      J. Setliff
    Function created. Investigate adding menu number and string to
    dictionary to use loop to print and improve switch functionality
"""
def PrintMenu():
    print("Welcome to iMenu - A shallow menu for shallow people")
    print("Please make a selection from the menu below (1 - 11)")
    print("1. Daily Affirmation"
          "\n2. Check your Twitter Follower count"
          "\n3. Turn screen into mirror"
          "\n4. Shop online to fill the void in your life"
          "\n5. Post a selfie to the Gram"
          "\n6. Waste an hour on Reddit"
          "\n7. Waste an hour and get upset on Facebook"
          "\n8. Leave a negative review at a local restaurant"
          "\n9. Go down a Youtube rabbit-hole"
          "\n10. TWO DIGITS? What am I, Einstein?"
          "\n11. Exit")

"""
Function: Clear()   Determine OS and issue command to clear terminal
Input Variables: none
Output Variables: none
Global Variables: none

Version History:
    08/16/2020      J. Setliff
    Function created.
"""
def Clear():

    # if windows
    if name == 'nt':
        _ = system('cls')

    # if unix
    else:
        _ = system('clear')

"""
Function: MenuSelection()   Python does not support switch/select case
                            Use dictionary to perform functionality
Input Variables:
            menuChoice      Integer value from main driver used to pick
                            correct function
Output Variables: none
Global Variables: none

Version History:
    08/16/2020      J. Setliff
    Function created. Investigate building out dictionary with ref
    values and function calls to simplify this.
"""
def MenuSelection(menuChoice):
    options = {
        1: MenuOne,
        2: MenuTwo,
        3: MenuThree,
        4: MenuFour,
        5: MenuFive,
        6: MenuSix,
        7: MenuSeven,
        8: MenuEight,
        9: MenuNine,
        10: MenuTen
    }
    return options.get(menuChoice)()

"""
Function: MenuOne() - MenuTen()     Stubbed functions. Contents TBD
Input Variables: none
Output Variables: none
Global Variables: none

Version History:
    08/16/2020      J. Setliff
    Functions created as stubs.
    *TO DO*: Figure out functionality and break out headers.
"""
def MenuOne():
    print("You're breathtaking!")
    print("DEBUG: Need to create a list of affirmations.")

def MenuTwo():
    print("It's just a number...")
    print("DEBUG: Figure out Twitter API")

def MenuThree():
    print("DEBUG: Silver spraypaint???")

def MenuFour():
    print("TODO: Create online store to compete with Amazon")

def MenuFive():
    print("You're breathtaking!")
    print("NOTE: Wait I've already done that one")

def MenuSix():
    print("reddit.com/r/ProgrammerHumor/")
    print("DEBUG: ERROR 404: JOKE NOT FOUND")

def MenuSeven():
    print("Let's not.")
    print("DEBUG: Find literally any other thing to replace this")

def MenuEight():
    print("DEBUG: Write script that only clicks One-Star")

def MenuNine():
    print("I recommend Chimpanzee Riding on a Segway")
    print("TODO: Research deep learning algorithm to mind-meld with user")

def MenuTen():
    print("e = mc^2")
    print("TODO: Solve unified theory")

"""
Function: WaitForEnter()        Prompt user to press return, waits for
                                input
Input Variables: none
Output Variables: none
Global Variables: none
Version History:
    08/16/2020      J. Setliff
    Function created.
"""
def WaitForEnter():
    print("\nPress Enter to Continue...")
    input()

"""
Main driver, will run if this .py is run on it's own, otherwise these
instruction will be ignored on import
"""
if __name__ == "__main__":
    # initialize menuChoice for use as while loop condition
    menuChoice = None

    # loop until user selects 11, the exit option
    while menuChoice != 11:
        """
        Call Clear function at the top of the loop to provide better
        presentation. Call PrintMenu function to display the menu to
        user. Try-Except-Else used to catch ValueErrors when user
        attempts to input a non-integer value, and If-Else statement
        used to validate integer value. 
        """

        Clear()
        PrintMenu()
        try:
            menuChoice = int(input())
        except:
            print()
            print("You must enter a value between 1-11")
            WaitForEnter()
        else:
            if 0 < menuChoice < 11:
                MenuSelection(menuChoice)
                WaitForEnter()
            elif menuChoice == 11:
                break
            else:
                print()
                print("You must enter a value between 1-11")
                WaitForEnter()