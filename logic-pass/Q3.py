# Q3/write a function that count how many the given character repeated in a given string?

def countChar(original_string, character):
    repute_number  = 0
    for a in original_string:
        if a == character:
            repute_number += 1
    print(repute_number)

countChar("Hello World","H")
