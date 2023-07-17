def multi():
    product = 1
    for num in range(1,24):
        product *= num
    return product

print(multi())