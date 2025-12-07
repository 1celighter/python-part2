# practicle for args and kwargs

# how it is might be look  def funct_name(*args, **kwargs):
#  and we can type our function like this maybe 

def shipping_lable(*args1, **kwargs1): # also we need type it like this if we type like this **, * we will get error 
    for arg in args1:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ") if we need get something from new line we can do it like this
    print(f"{kwargs1.get('name')}, {kwargs1.get('apt')}") # ATTENTION! we must use a single '' or python will be confused 
    print(f"{kwargs1.get('street')} {kwargs1.get('type')}") # if we write it on one line we do it
    print(f"{kwargs1.get('apt0')}") # if we want type a apt but we dont have it we will get this in ressult - None
    

shipping_lable("just name here", "we can feel free here", "that all also is args", # we can understand it with "" and * at function def
        name="james",
        street="omagat courpse 3",
        apt="#012",
        type="that all is kwargs now hehe" # we can understand it with funct name and = and like args with ** 
)

print()
print() # for more readability no worry i am not crazy
print()
# but what if we dont want getting none as result we can do this~ 

def ship(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else: print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

ship("Dr.", "James", "Jemty",
    street="random street 351",
    state="Origon",
    pobox="PO box #3459",
    zip="12357")