import string
import itertools

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r

def generate_strings(length=5):
    chars = string.ascii_letters + string.digits  # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)

def crack(s):
    length_of_each_gamble = len(s)
    #for string in itertools.imap(''.join, itertools.product('ABC', repeat=3)):
    chars = string.ascii_letters + string.digits  # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for item in itertools.product(chars, repeat=length_of_each_gamble):
        gamblei = "".join(item)
        if (simple_hash(gamblei) == simple_hash(s)) and (s!= gamblei):
            print(gamblei)
            break

crack('aba')
    #return # return s2 such that s != s2 and simple_hash(s) == simple_hash(s2)
