# ******************************************************************************
# Author:           Luke Helfinstine
# Lab:              Lab 3
# Date:             February 5, 2022
# Description:      This calculator tells you how many boxes of diapers you
#                   need to buy each week based on the number of children
#                   you have and how many diapers each child uses per day.
#                   The most recent update adds options for different box
#                   counts; 32, 84, and 162, and rounds the total number of
#                   boxes needed up to a whole number.
# Input:            Integers for number of children and number of diapers per
#                   day.
# Output:           A total number of boxes of 84 diapers the user needs to buy
#                   each week.
# Sources:          Target website and Walmart website for diaper box counts and
#                   prices. NOTE: All prices based on newborn size.
# ******************************************************************************
# Example output:
# How many children do you have? 2
# How many diapers does each child use per day? 3
# Do you shop at Target or Walmart? Please type:
# If you buy boxes of 31 from Walmart, you will need to buy 2 boxes of diapers a week for
# $9.56 per box.
# ******************************************************************************
# TO DO: Create function that adds the total amount due for the total number of
#        boxes and displays the new amount.
# ******************************************************************************


# Import math

import math


# Module main()
#     declare constant BOX_DIAPERS_1 = 31
#     declare constant BOX_DIAPERS_2 = 84
#     declare constant BOX_DIAPERS_3 = 140
#
#     call numKids = getKids()
#     call numDiapers = getDiapers()
#     call whichStore = getStore()
#
#     call calcDiapers(numKids, numDiapers, BOX_DIAPERS_1, BOX_DIAPERS_2, BOX_DIAPERS_3, whichStore)
#
#     display "If you buy boxes of X from Y, you'll need to buy", Z,
#             "boxes of diapers a week for $A.BC!"
# End module

def main():
    BOX_DIAPERS_1 = 31
    BOX_DIAPERS_2 = 84
    BOX_DIAPERS_3 = 140

    numKids = getKids()
    numDiapers = getDiapers()
    whichStore = getStore()

    calcDiapers(numKids, numDiapers, BOX_DIAPERS_1, BOX_DIAPERS_2, BOX_DIAPERS_3, whichStore)


# Module getKids()
#     Display "enter number of kids"
#     input numKids
#     return numKids
# End module

def getKids():
    numKids = int(input("How many kids do you have? "))
    return numKids


# Module getDiapers()
#     display "enter number of diapers"
#     input numDiapers
#     return numDiapers
# end module

def getDiapers():
    numDiapers = float(input("How many diapers does each one use per day? "))

    return numDiapers


# Module getStore()
#   display "do you shop at Target or Walmart?"
#   input whichStore
#   return whichStore
# end module

def getStore():
    whichStore = str(input("Do you shop at Target or Walmart? Please type: "))
    return whichStore


# Module calcDiapers(integer numKids, float numDiapers, constant BOX_DIAPERS_1, constant BOX_DIAPERS_2,
#                   constant BOX_DIAPERS_3, string whichStore)
#     set totalDiapers = numKids * numDiapers * 7
#
#     if totalDiapers > 140 Then
#           final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_3))
#           display 'If you buy boxes of 140 from', whichStore, 'you will need to buy', final, 'boxes
#                    of diapers a week for $42.94')
#
#      elif totalDiapers > 84 Then
#           final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_2))
#           display 'If you buy boxes of 84 from', whichStore, 'you will need to buy', final, 'boxes
#                    of diapers a week for $27.22')
#      elif totalDiapers > 32 Then
#           final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_1))
#           display 'If you buy boxes of 31 from', whichStore, 'you will need to buy', final, 'boxes
#                    of diapers a week for $9.56'
#
#  ### repeat process for Target with Target prices (use google) ###
#
#      return totalDiapers
#
# end module

def calcDiapers(numKids, numDiapers, BOX_DIAPERS_1, BOX_DIAPERS_2, BOX_DIAPERS_3, whichStore):
    totalDiapers = ((numKids * numDiapers) * 7)
    if whichStore == "Walmart":
        if totalDiapers > 140:
            final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_3))
            print('If you buy boxes of 140 from ', whichStore, ', you will need to buy', final,
                  'boxes of diapers a week for $42.94 per box.')

        elif totalDiapers > 84:
            final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_2))
            print('If you buy boxes of 84, you will need to buy', final, 'boxes of diapers a week for'
                                                                         '$27.22 per box.')

        elif totalDiapers > 31:
            final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_1))
            print('If you buy boxes of 31, you will need to buy', final, 'boxes of diapers a week for '
                                                                         '$9.56 per box.')

    if whichStore == "Target":
        if totalDiapers > 140:
            final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_3))
            print('If you buy boxes of 140 from ', whichStore, ', you will need to buy', final,
                  'boxes of diapers a week for $42.99 per box.')

        elif totalDiapers > 84:
            final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_2))
            print('If you buy boxes of 84, you will need to buy', final,
                  'boxes of diapers a week for $27.99.')

        elif totalDiapers > 31:
            final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_1))
            print('If you buy boxes of 31, you will need to buy', final,
                  'boxes of diapers a week for $9.59 per box.')

    return totalDiapers


main()
