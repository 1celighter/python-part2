# ** kwargs meaning is arguments but with keyword agrument if talk by the way that similar like def_keyword

def print_adress(**kwargs):
    for value in kwargs.values():
        print(value)
print_adress(street="some_text here", any="just need to text here any argument what we want")