def nearest_palindrome(number):
    number=number+1
    s=str(number)
    if s == s[::-1]:
        return number
    else:
        return nearest_palindrome(number)
    #start writitng your code here
number=12300
print(nearest_palindrome(number))
