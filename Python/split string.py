#Complete the solution so that it splits the string into pairs of two characters. 
#f the string contains an odd number of characters then it should replace the missing 
#second character of the final pair with an underscore ('_').
#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python

def solution(s):  
    if len(s)<=1:
        if len(s)==0:
            return []
        else:
            return [s+'_']
    return [s[0:2]]+solution(s[2:])

#refact code 
import re
def solution(s):
    return re.findall(".{2}", s + "_")