import string

user_input = input("Введіть літери через дефіс (наприклад, a-z): ")
start_char, end_char = user_input.split('-')
letters = string.ascii_letters
start_index = letters.index(start_char)
end_index = letters.index(end_char)

print(letters[start_index : end_index + 1])