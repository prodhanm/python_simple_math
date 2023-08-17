def multi():
    try:
        product = 1
        for num in range(1,24):
            product *= num
        return product
    except ValueError as err:
        print(err)

print(multi())

def multi_list():
    try:
        prod_li = [num*2 if num%2 == 0 else num//2 
                   for num in range(1,24)]
        return prod_li
    except ValueError as err:
        print(err)

print(f"products = {multi_list()}")

def li_comp():
    try:
        num_li = [num for num in range(1,24)]
        return num_li
    except ValueError as err:
        print(err)

def app_mult():
    try:
        double_nums = []
        for nums in range(len(li_comp())):
            double_nums.append(li_comp()[nums]*2)
        return double_nums
    except ValueError as err:
        print(err)

print(f"double multiples = {app_mult()}")

def square():
    try:
        square_li = [li_comp()[num]**2 for num in range(len(li_comp()))]
        return square_li
    except ValueError as err:
        print(err)

print(f"sqaured numbers = {square()}")

def tot():
    try:
        total = sum(li_comp())
        return total
    except ValueError as err:
        print(err)

print(f"The total of the list from li_comp() is {tot()}")

def average():
    try:
        avg = tot()/len(li_comp())
        return avg
    except ValueError as err:
        print(err)

print(f"The average of the list comprehension from li_comp() is {average()}")

def subtr():
    try:
        diff = 0
        for num in range(len(li_comp())):
            diff -= li_comp()[num]
        return diff
    except ValueError as err:
        print(err)

print(f"The differnce of all of the numbers from the list in li_comp() is {subtr()}")

def straight():
    try:
        floor_avg = tot()//len(li_comp())
        return floor_avg
    except ValueError as err:
        print(err)

print(f"The floor average of the list from li_comp() is {straight()}")

def diff_floor():
    try:
        diff_avg = subtr()//len(li_comp())
        return diff_avg
    except ValueError as err:
        print(err)
        
print(f"The floor average of the values subtracted in li_comp() is {diff_floor()}")
