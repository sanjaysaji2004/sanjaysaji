a=int(input("enter the number:"))
def is_palindrome(x):
        return str(x) == str(x)[::-1]
print("the entered number is palindrome or not (true/false):",is_palindrome(a))
