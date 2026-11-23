def count_vowels():
    s = "Python Programming"
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    print("Vowels:", count)

count_vowels()