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
# Sources:          Target website for box counts.
# ******************************************************************************
# Example output:
# How many children do you have? 2
# How many diapers does each child use per day? 3
# If you buy boxes of 32, you'll need to buy 2 boxes of diapers a week!
# ******************************************************************************

# Import math

import math


# Module main()
#     declare constant BOX_DIAPERS = 84
#     declare integer numKids
#     declare float numDiapers
#
#     call numKids = getKids()
#     call numDiapers = getDiapers()
#
#     call calcDiapers(numKids, numDiapers, BOX_DIAPERS_1, BOX_DIAPERS_2, BOX_DIAPERS_3)
#
#     display "If you buy boxes of X, you'll need to buy", final,
#       "boxes of diapers a week!"
# End module

def main():
    totalDiapers = 0

    BOX_DIAPERS_1 = 31
    BOX_DIAPERS_2 = 84
    BOX_DIAPERS_3 = 140

    numKids = getKids()
    numDiapers = getDiapers()
    whichStore = getStore(totalDiapers)

    price = getStore()

    calcDiapers(numKids, numDiapers, BOX_DIAPERS_1, BOX_DIAPERS_2, BOX_DIAPERS_3, whichStore, price)


# Module getKids()
#     declare integer numKids
#     Display "enter number of kids"
#     input numKids
#     return numKids
# End module

def getKids():
    numKids = int(input("How many kids do you have? "))
    return numKids


# Module getDiapers()
#     declare float numDiapers
#     display "enter number of diapers"
#     input numDiapers
#     return numDiapers
# end module

def getDiapers():
    numDiapers = float(input("How many diapers does each one use per day? "))

    return numDiapers


# Module getStore()
# declare boolean
# display "do you shop at Target or Walmart?"
# input whichStore
# set price if Walmart
# set price if Target
# return whichStore

def getStore(totalDiapers):
    whichStore = str(input("Do you shop at Target or Walmart? Please type: "))
    if whichStore == "Walmart":
        if totalDiapers >= 140:
            price = str("$48")
            return price
        if totalDiapers >= 82:
            price = "$28"
            return price
    return whichStore


# WLMRT_PRICE_1 = "$9.56"
# WLMRT_PRICE_2 = "$27.22"
# WLMRT_PRICE_3 = "$42.94"
#
# TRGT_PRICE_1 = "$9.59"
# TRGT_PRICE_2 = "$27.99"
# TRGT_PRICE_3 = "$42.99"


# def getPrice(whichStore, totalDiapers, price):
#     if whichStore == 'Walmart':
#         if totalDiapers >= 140:
#             price = "$48"
#         return price
#
#     if whichStore == "Target":
#         if totalDiapers >= 140:
#             price = "$42"
#         return price


# Module calcDiapers(integer numKids, float numDiapers, constant BOX_DIAPERS_1, constant BOX_DIAPERS_2,
#                   constant BOX_DIAPERS_3)
#     declare integer totalDiapers
#
#     set totalDiapers = numKids * numDiapers * 7
#
#     if totalDiapers > 162 Then
#           final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_3))
#           print('If you buy boxes of 162, you will need to buy', final, 'boxes of diapers a week!')
#
#      elif totalDiapers > 84 Then
#           final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_2))
#           print('If you buy boxes of 84, you will need to buy', final, 'boxes of diapers a week!')
#
#      elif totalDiapers > 32 Then
#           final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_1))
#           print('If you buy boxes of 32, you will need to buy', final, 'boxes of diapers a week!')
#
#     return totalDiapers
# end module

def calcDiapers(numKids, numDiapers, BOX_DIAPERS_1, BOX_DIAPERS_2, BOX_DIAPERS_3, whichStore, price):
    totalDiapers = ((numKids * numDiapers) * 7)

    if totalDiapers > 140:
        final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_3))
        print('If you buy boxes of 140 from ', whichStore, ', you will need to buy', final,
              'boxes of diapers a week for,', print(price), '.')

    elif totalDiapers > 84:
        final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_2))
        print('If you buy boxes of 84, you will need to buy', final, 'boxes of diapers a week.')

    elif totalDiapers > 31:
        final = (math.ceil(numKids * numDiapers * 7 / BOX_DIAPERS_1))
        print('If you buy boxes of 31, you will need to buy', final, 'boxes of diapers a week.')

    return totalDiapers


#####

main()
