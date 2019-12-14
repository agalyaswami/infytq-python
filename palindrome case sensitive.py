def is_palindrome(word):
    word.lower()
    if word[::-1].lower() ==word.lower():
        return 1
    else:
        return 0
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
