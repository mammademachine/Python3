#Giraffe Language
#vowels -> g
#-----------------
#
#dog -> dgg
#cat -> cgt
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "G"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))