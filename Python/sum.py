#DESCRIPTION:
#Write a function that takes an array of numbers and returns the sum of the numbers. T
# he numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

#Examples
#Input: [1, 5.2, 4, 0, -1]
#Output: 9.2

#Input: []
#Output: 0

#Input: [-2.398]
#Output: -2.398

def sum_array(a):
    return sum(a) if a else 0