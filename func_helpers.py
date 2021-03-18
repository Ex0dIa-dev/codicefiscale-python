#module for string manipulation
import datetime

def get_vocals(s):
    vocals = ['a', 'e', 'i', 'o', 'u']
    n = 0
    finded_vocals = []

    for ch in s.lower():
        if ch in vocals:
            n = n+1
            finded_vocals.append(ch)
    
    return finded_vocals, n

def get_cons(s):
    vocals = ['a', 'e', 'i', 'o', 'u']
    n = 0
    finded_cons = []

    for ch in s.lower():
        if ch not in vocals:
            n = n+1
            finded_cons.append(ch)
    
    return finded_cons, n


def validate_date(d):
    
    try:
        datetime.datetime.strptime(d, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Not valid date format: should be DD/MM/YYYY")