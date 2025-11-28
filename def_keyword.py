# keyword arguments = an argument preceded by an identifier
# help with readability
# order of arguments doesnt matter
# 1. positional, 2. default, 3. KEYWORD, 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


hello("Hi", "Mr.", "crabs", "none")  # that a positional

hello(
    greeting="yo", title="mr.", last="squarepants", first="spongebob"
)  # that a keyword


def get_phone(country, area, first2, last2):
    return f"{country}-{area}-{first2}-{last2}"


phone_num = get_phone(country=1, area=490, first2=312, last2=1204)
print(phone_num)
