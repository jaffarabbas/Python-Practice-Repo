# remove dublicate character from string and return it

def remove_dublicate(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string

print(remove_dublicate("Hello World!"))

# remove dublicate character which are next to each other e.g apple pp from string and return it

def remove_dublicate_next(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] != string[i-1]:
            new_string += string[i]
    return new_string

print(remove_dublicate_next("Jaffar"))