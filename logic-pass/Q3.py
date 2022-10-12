def countChar(original_string, character):
    repute_number  = 0
    for char in original_string:
        if char == character:
            repute_number += 1
    print(repute_number)

countChar("Hello World","H")
