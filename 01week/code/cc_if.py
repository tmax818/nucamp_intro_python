# Turn lines 1 through 10 into a multi-line comment using a pair of triple quotes. All that's left is an if/else statement that checks if 0 is equal to 100.

"""
Students | Grades | Letters
------------ | ---------- | ----------
George | 46 | F
Michell | 80 | B
Josh | 12 | F
Chloe | 68 | D
Stanley | 99 | A
Annie | 100 | A+
"""

# Declare a variable on line 11, above the first conditional if statement. Name it gradeToTest and assign it the value of 0.

gradeToTest = 100

# Replace the number 0 on line 12 with gradeToTest.

if gradeToTest == 100:
    # If a student has a grade of 100, the program should print out "A+". Replace the "Passing" string in the print function on line 13 with "A+".
    print("A+")
# Underneath the first if statement, you will need to create several elif statements for the grades A, B, C, and D:
# On line 14, create a new elif statement that checks to see if gradeToTest is greater than or equal to 90. If so, then on line 15 print "A".
elif gradeToTest >= 90:
    print("A")
# On line 16, create another elif statement that checks to see if gradeToTest is greater than or equal to 80. If so, then on line 17 print "B".
elif gradeToTest >= 80:
    print("B")
# On line 18, create another elif statement that checks to see if gradeToTest is greater than or equal to 70. If so, then on line 19 print out "C".
elif gradeToTest >= 70:
    print("C")
# On line 20, create another elif statement that checks to see if gradeToTest is greater than or equal to 50. If so, then on line 21 print out "D".
elif gradeToTest >= 50:
    print("D")
# For the else statement, replace the string "Failing" with "F". This will be the default case.
else:
    print("F")

# Finally, open the integrated terminal in Visual Studio Code. You can do this either by going to the View menu and selecting Terminal, or using the keyboard shortcut Ctrl/Control + ` <-- this character is a backtick character, not a single quote, and you can find it just below your Esc button at the top left of your keyboard.
# In the terminal, run your code by entering:
# python cc-if.py

# If the Python interpreter gives you an error message when you try to run your code, read the message and try to figure out what it means. It will only give you a hint about the first error message it encounters. Once you fix that one, try running your code again. If you have another bug in your code further down, you will see a new error message.

# If you encounter an error message that you cannot fix, try to fix it on your own for 20 minutes, reviewing the material in the previous lessons. Remember the 20-minute rule! Once you have reached the 20-minute mark, go to the Nucamp Slack and reach out there for help.0
