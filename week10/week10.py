import math
# Exercises 1

mylist = [76,92.3,"hello",True,4,76]
mylist.append("apple")
mylist.append(76)
mylist.insert(0 ,99)
mylist.index("hello")
mylist.count(76)
mylist.remove(76)
mylist.pop(mylist.index(True))
# print(mylist)

# Exercises 2

def sum_of_squares(list):
    sum = 0
    for i in list:
        sum += i**2
    return sum

# print(sum_of_squares([2,3,4]))

# Exercises 3

def sum_up_even(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    return even

# print(sum_up_even([5,12,8,6,21]))

# Exercises 4

def count_the_lenght(list):
    count = 0
    for i in list:
        if len(i) == 5:
            count += 1
    return count

# print(count_the_lenght(["apple","banana","kalem","araba","ucak"]))

# Exercises 5

def sum_until_first_even(list):
    sum = 0
    for i in list:
        if i % 2 == 1:
            sum += i

        if i % 2 == 0:
            break
    return sum

# print(sum_until_first_even([5,11,9,6,21]))

# Exercises 6

def count_until_first_sam(list):
    l = []
    for i in list:
        l.append(i)

        if i == "sam":
            break

    print(l)
    return len(l)

# print(count_until_first_sam(["apple","banana","kalem","araba","sam","ucak"]))

# Exercises 7

def replace(text, old, new):
    new_text = text.split(old)
    return new.join(new_text)

# print(replace("I love spom! Spom is my favourite food. Spom, spom, spom, spom, yum!", "om", "ommm"))

# Exercises 8

def find_max(list):
    max = 0
    for i in list:
        if i >max:
            max = i
    return max

print(find_max([550,1240,330,1241,335]))