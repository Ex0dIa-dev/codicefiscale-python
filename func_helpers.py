#module for string manipulation
import datetime

#return a list of vowals, and the total of vowals
def get_vocals(s):

    return [v for v in s.lower() if v in "aeiou"], sum([1 for v in s.lower() if v in "aeiou"])

#return a list of cons, and the total of cons
def get_cons(s):

    return [c for c in s.lower() if c not in "aeiou"], sum([1 for c in s.lower() if c not in "aeiou"])
    
def validate_date(d):
    
    try:
        datetime.datetime.strptime(d, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Not valid date format: should be DD/MM/YYYY")