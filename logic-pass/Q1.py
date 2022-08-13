# Q1/Write a method that will remove any given character from a String?

original_string = "Hello World"
character_remove = "e"
new_string = ""

for a in original_string:
    if a != character_remove:
        new_string += a
print(new_string)
