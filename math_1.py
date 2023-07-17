def multi():
    product = 1
    for num in range(1,24):
        product *= num
    return product

print(multi())

def multi_list():
    prod_li = [num*2 if num%2 == 0 else num//2 
               for num in range(1,24)]
    return prod_li

print(f"products = {multi_list()}")

def li_comp():
    num_li = [num for num in range(1,24)]
    return num_li

def app_mult():
    double_nums = []
    for nums in range(len(li_comp())):
        double_nums.append(li_comp()[nums]*2)
    return double_nums

print(f"double multiples = {app_mult()}")

def square():
    square_li = [li_comp()[num]**2 for num in range(len(li_comp()))]
    return square_li

print(f"sqaured numbers = {square()}")

def tot():
    total = sum(li_comp())
    return total

print(f"The total of the list from li_comp() is {tot()}")

def average():
    
    avg = tot()/len(li_comp())
    return avg

print(f"The average of the list comprehension from li_comp() is {average()}")

def subtr():
    diff = 0
    for num in range(len(li_comp())):
        diff -= li_comp()[num]
    return diff

print(f"The differnce of all of the numbers from the list in li_comp() is {subtr()}")

def straight():
    floor_avg = tot()//len(li_comp())
    return floor_avg

print(f"The floor average of the list from li_comp() is {straight()}")

def diff_floor():
    diff_avg = subtr()//len(li_comp())
    return diff_avg

print(f"The floor average of the values subtracted in li_comp() is {diff_floor()}")
