#******************************************************************************
# Author:           Luke Helfinstine
# Lab:              Lab 2
# Date:             Jan 17, 2021
# Description:      This calculator tells you how many boxes of diapers you
#                   need to buy each week based on the number of children
#                   you have and how many diapers each child uses per day.
# Input:            Integers for number of children and number of diapers per
#                   day.
# Output:           A total number of boxes of 84 diapers the user needs to buy
#                   each week.
# Sources:          Target website for box counts.
#******************************************************************************
# Example output:
# How many children do you have? 2
# How many diapers does each child use per day? 3
# If you buy boxes of 84, you'll need to buy 0.5 boxes of diapers a week! Holy moly!!
#******************************************************************************

#Declare Integer numKids
#Declare Real numDiapers
#Declare Constant Integer BOX_DIAPERS

#Display "How many children do you have?"
#Input numKids

#Display "How many diapser does each child use per day?"
#Input numDiapers

#Set totalDiapers = numKids * numDiapers * 7 (days)

#Set weeklyDiapers = totalDiapers / BOX_DIAPERS

#Display "If you buy boxes of 84,
#         you'll need to buy X boxes of diapers a week!"

#End

#------------------------------------------------------------------------------

#Declare Integer numKids
#Declare Real numDiapers
#Declare Constant Integer BOX_DIAPERS
numKids = 0
numDiapers = 0.0
BOX_DIAPERS = 84

#Display "How many children do you have?"
#Input numKids
numKids = int(input("How many children do you have? "))

#Display "How many diapser does each child use per day?"
#Input numDiapers
numDiapers = float(input("How many diapers does each child use per day? "))

#Set totalDiapers = numKids * numDiapers * 7 (days)
totalDiapers = numKids * numDiapers * 7

#Set weeklyDiapers = totalDiapers / BOX_DIAPERS
weeklyDiapers = totalDiapers / BOX_DIAPERS

#Display "If you buy boxes of 84,
#         you'll need to buy X boxes of diapers a week!"
print("If you buy boxes of 84, you'll need to buy", weeklyDiapers,
      "boxes of diapers a week! Holy moly!!")
# Ask in lecture how to round this number up to the nearest whole, real number.

#End
exit()