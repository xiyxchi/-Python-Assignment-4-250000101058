def palindrome():
    s = "madam"
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome()