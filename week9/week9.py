# EXERCİSE 1
def is_oddHayır(n):
    if n % 2 == 1:
        return True
    else :
        return False


# EXERCİSE 2
def if_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# EXERCİSE 3
def print_triangular_number(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        print(i,total)


# EXERCİSE 4

def if_prime(n):
    if n % 2 == 0:
        if n < 2:
            return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


# EXERCİSE 5
def reverse(text):
    reversed_text = ""
    for n in (text):
        reversed_text = n + reversed_text
    return(reversed_text)

# print(reverse("abc"))


def reverse_slice(s):
    return s[::-1]
# print(reverse_slice("abc"))

# EXERCİSE 6
def remove_all(sub , s):
    return s.replace(sub, "")

# print(remove_all("n", "banana"))

# EXERCİSE 7
def substitution_cipher(message,key):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for ch in message:
        index = alfabet.find(ch.lower())
        if index == -1:
            result += result + ch
        elif ch.isupper():
            result = result + key[index].upper()
        else:
            result = result + key[index].lower()
    return result
key = "qwertyuiopasdfghjklzxcvbnm"

print(substitution_cipher("buğra", key))

# EXERCİSE 8
def remove_dups(s):
    new_s = ""
    for ch in s:
        if ch in new_s:
            pass
        else:
            new_s += ch
    return new_s
print(remove_dups("buuggraa"))