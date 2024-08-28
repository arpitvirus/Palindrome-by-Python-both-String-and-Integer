# Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome (a word, phrase, or sequence that reads the same backward as forward), and False otherwise.


# def is_palindrome(s):
#     # Remove any spaces and convert the string to lowercase
#     s = s.replace(" ", "").lower()
#     print(s)
#     b = s[::-1]
#     print(b)

#     # Check if the string is equal to its reverse
#     return s == s[::-1]

# print(is_palindrome("Hello"))



def num(n):
    b =  n[::-1]
    if(b==n):
        print("Your number is Palindrome:",b)
    else:
        print("Your Number is not a palindrome")

num(input("Enter The number : "))