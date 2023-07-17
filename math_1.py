def multi():
    product = 1
    for num in range(1,24):
        product *= num
    return product

print(multi())

def multi_list():
    prod_li = [num*2 if num%2 == 0 else num//2 for num in range(1,24)]
    return prod_li

print(f"products = {multi_list()}")