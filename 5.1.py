import string
import keyword

my_str = "some_super_puper_value"

if my_str in keyword.kwlist:
    print(False)
elif len(my_str) == 0 or my_str[0].isdigit():
    print(False)
elif any(char.isupper() for char in my_str):
    print(False)
elif any((char in string.punctuation and char != '_') or char == ' ' for char in my_str):
    print(False)
elif my_str.count('_') == len(my_str) and len(my_str) > 1:
    print(False)
else:
    print(True)