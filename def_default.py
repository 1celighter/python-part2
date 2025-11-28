# default arguments = a default value for certain parameters default is used when that argument is omitted
# make your function more flexible, reduces # of arguments
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary
import time


def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500, 0, 0.05))

# we also can write this with another way  like that and we get a same result


def net_price2(list_price2, discount2=0, tax2=0.05):
    return list_price2 * (1 - discount2) * (1 + tax2)


print(net_price2(500))

# we can also change on this function all ours arguments in print
print(
    net_price2(420, 0.1, 0)
)  # there we are write first argument seceond and third that useful and make our functions more flexible


# exercise with time
def count(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")


count(0, 10)

# but also we got one problem here if we want write our count we must write it like that def count(end, start=0) atleast def count (start=0,end)
# we just get error because


def count(end, start=30):
    for y in range(start, end + 1):
        print(y)
        time.sleep(1)
    print("done!")


count(33)  # here we are getting (end , start=30)
