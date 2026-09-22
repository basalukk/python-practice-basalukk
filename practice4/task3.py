print("Illia Basalukk, IT-31")

name = "Illia"
surname = "Basalukk"

text = name + surname
vowels = "aeiouy"

vowels_count = 0
consonants_count = 0

for char in text:
    if char.lower() in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"{name} {surname}")
print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
print(f"Total letters: {len(text)}")
print(f"Check: {vowels_count + consonants_count} == {len(text)}")