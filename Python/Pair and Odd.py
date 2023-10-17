# describtion : Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# Solution

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Pour tester la fonction :
num = 3
print(even_or_odd(num))  # Affichera "Odd"
