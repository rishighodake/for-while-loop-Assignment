text = input("Enter a string: ")
consonant_count = 0

for character in text:
    if character.isalpha() and character.lower() not in "aeiou":
        consonant_count += 1

print(f"Number of consonants: {consonant_count}")
