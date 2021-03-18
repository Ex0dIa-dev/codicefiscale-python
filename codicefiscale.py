import func_helpers as fs
import csv
from string import digits

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

    month_char = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'H',
        7: 'L',
        8: 'M',
        9: 'P',
        10: 'R',
        11: 'S',
        12: 'T',
    }

    #check if date is valid
    fs.validate_date(date)

    day, month, year = map(int, date.split('/'))

    
    
    if sex.upper() == 'M':

        if day > 10:
            return str(year)[2:] + month_char[month] + str(day)
        else: 
            return str(year)[2:] + month_char[month] + '0' + str(day)
        
    elif sex.upper() == 'F':
        return str(year)[2:] + month_char[month] + str(day + 40)


def GetCityCode(city):

    with open("data/comuni.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == city.upper():
                return row[1]
    
def GetControlCode(cf):

    control_code = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z'
    }


    char_odd_value= {
        "A":"0",
        "B":"1",
        "C":"2",
        "D":"3",
        "E":"4",
        "F":"5",
        "G":"6",
        "H":"7",
        "I":"8",
        "J":"9",
        "K":"10",
        "L":"11",
        "M":"12",
        "N":"13",
        "O":"14",
        "P":"15",
        "Q":"16",
        "R":"17",
        "S":"18",
        "T":"19",
        "U":"20",
        "V":"21",
        "W":"22",
        "X":"23",
        "Y":"24",
        "Z":"25"
    }

    char_even_value={
        "0":"1",
        "1":"0",
        "2":"5",
        "3":"7",
        "4":"9",
        "5":"13",
        "6":"15",
        "7":"17",
        "8":"19",
        "9":"21",
        "A":"1",
        "B":"0",
        "C":"5",
        "D":"7",
        "E":"9",
        "F":"13",
        "G":"15",
        "H":"17",
        "I":"19",
        "J":"21",
        "K":"2",
        "L":"4",
        "M":"18",
        "N":"20",
        "O":"11",
        "P":"3",
        "Q":"6",
        "R":"8",
        "S":"12",
        "T":"14",
        "U":"16",
        "V":"10",
        "W":"22",
        "X":"25",
        "Y":"24",
        "Z":"23"
        }

    #check if the len is correct
    assert len(cf) == 15

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
    

    tot = 0
    for x in peer_ch:
        if x in digits:
            tot += int(x)
        else:
            tot += int(char_odd_value[x])
    
    for x in even_ch:
        tot += int(char_even_value[x])

    
    return control_code[tot%26]

def CalcolaCodiceFiscale(surname, name, date, sex, city):

    cf = ""
    
    cf += GetSurname(surname)
    cf += GetName(name)
    cf += GetBirthday(date, sex)
    cf += GetCityCode(city)
    cf += GetControlCode(cf)

    return cf







    
    
