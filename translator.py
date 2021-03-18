#building a basic translator. for eg: english to a made up language
def translate(phrase):
    translation = ""
    for item in phrase:
        if item.upper() in "AEIOU":
            if item.islower():
                translation = translation + "g"
            else:    
                translation = translation + "G"

        else:
            translation = translation + item

    return translation

print(translate(input("please enter a phrase:  ")))                