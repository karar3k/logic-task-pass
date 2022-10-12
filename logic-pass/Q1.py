def check_character(original_string, character_remove):
    new_string = ""
    for character in original_string:
        if character != character_remove:
            new_string += character
    print(new_string)

check_character("Hello World","e")
