def main():
    word = str(input("Input: "))
    vowel_removed = ""
    for letter in word:
        if is_vowel(letter):
            letter = ""
        vowel_removed += letter
    print(vowel_removed)

def is_vowel(l):
    l = l.lower()
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        return l
    
main()