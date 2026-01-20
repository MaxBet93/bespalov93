import string

def create_hashtag(s: str) -> str:
    s = s.title()
    clean_string = "".join(
        char for char in s
        if char not in string.punctuation and char != " "
    )
    hashtag = "#" + clean_string
    return hashtag[:140]
print(create_hashtag("Hello world"))
print(create_hashtag("   Hello     world   "))
print(create_hashtag("python is, awesome!"))
print(create_hashtag("codewars is nice"))