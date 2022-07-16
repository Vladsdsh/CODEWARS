# Considérez un tableau/une liste de moutons où certains moutons peuvent manquer à leur place. 
# Nous avons besoin d'une fonction qui compte le nombre de moutons présents dans le tableau (vrai signifie présent).
# Par exemple,
# https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    count=0
    for i in sheep:
        if i == True:
            count= count + 1
    return count