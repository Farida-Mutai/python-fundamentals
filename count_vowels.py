def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

result = count_vowels("farida")
print(result)  # Output will be 3

result = count_vowels("monster high")
print(result)  # Output will be 3
