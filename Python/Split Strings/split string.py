#Complete the solution so that it splits the string into pairs of two characters. 
#f the string contains an odd number of characters then it should replace the missing 
#second character of the final pair with an underscore ('_').


def solution(s):  
    if len(s)<=1:
        if len(s)==0:
            return []
        else:
            return [s+'_']
    return [s[0:2]]+solution(s[2:])