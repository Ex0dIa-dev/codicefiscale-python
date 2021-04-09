import func_helpers as fs
import csv
from string import digits
import data.dicts as dicts 

def GetSurname(surname):

    cons, n = fs.get_cons(surname)
    vocs, _ = fs.get_vocals(surname)

    if n >= 3:
        return (cons[0] + cons[1] + cons[2]).upper()
    elif n == 2:
        return (cons[0] + cons[1] + vocs[0]).upper()
    elif n == 1:
        return (cons[0] + vocs[0] + vocs[1]).upper()


def GetName(name):

    cons, n = fs.get_cons(name)
    vocs, _ = fs.get_vocals(name)

    if n >= 4:
        return (cons[0] + cons[2] + cons[3]).upper()
    elif n == 3:
        return (cons[0] + cons[1] + cons[2]).upper()
    elif n == 2:
        return (cons[0] + cons[1] + vocs[0]).upper()
    elif n == 1:
        return (cons[0] + vocs[0] + vocs[1]).upper()


# dd/mm/yyyy
def GetBirthday(date, sex):

    

    #check if date is valid
    fs.validate_date(date)

    day, month, year = map(int, date.split('/'))

    if sex.upper() == 'M':

        if day > 10:
            return str(year)[2:] + dicts.month_char[month] + str(day)
        else: 
            return str(year)[2:] + dicts.month_char[month] + '0' + str(day)
        
    elif sex.upper() == 'F':
        return str(year)[2:] + dicts.month_char[month] + str(day + 40)


def GetCityCode(city):

    with open("data/comuni.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == city.upper():
                return row[1]
    

def GetControlCode(cf):
    
    assert(len(cf) == 15), "Lunghezza Codice Fiscale Errata"

    n = 0
    even_ch = []
    peer_ch = []

    #taking even chars and peer chars
    for c in cf:
        if n % 2 == 0:
            even_ch.append(c)
        else:
            peer_ch.append(c)
        
        n += 1

    tot = sum([int(x) if x in digits else int(dicts.char_odd_value[x]) for x in peer_ch])
    tot += sum([int(dicts.char_even_value[x]) for x in even_ch])

    return dicts.control_code[tot%26]


def CalcolaCodiceFiscale(surname, name, date, sex, city):

    cf = ""
    
    cf += GetSurname(surname)
    cf += GetName(name)
    cf += GetBirthday(date, sex)
    cf += GetCityCode(city)
    cf += GetControlCode(cf)

    return cf







    
    
