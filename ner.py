# -*- coding: utf-8 -*-
import sys
import re
import locations
import organizations
import person
import date


# Input and Output files
input_file_path = sys.argv[1]
f = open(input_file_path, "r")
input_file = f.read()


# Locations
CITIES = locations.cities  #+
COUNTRIES = locations.countries  #+
CONTINENTS = locations.continents  #+
CAPITALS = locations.capitals  #+
LOCATIONS = locations.locations  #+

# Person
PERSON = person.person  #+
PRE_PERSON = person.pre_person  #+
POST_PERSON = person.post_person  #+
MAN = person.man_names          #+
WOMAN = person.woman_names      #+
ADJ_NOUN = person.adjective_noun #+

# Organizations
ORGANIZATION = organizations.organization  #+
POST_ORGANIZATIONS = organizations.post_organization  #+
COMPANIES = organizations.companies #+

# Time
TIME = date.time  # +

# POST_TIME = time.post_time
MONTHS = date.months  # +

line_count = 1

for line in input_file.splitlines():

    # Person
    for i in PERSON:
        if i in line:
            print("Line ", line_count, ": PERSON ", i)

    for i in POST_PERSON:
        if i in line and re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ' + i, line) != []:
            print("Line ", line_count, ": PERSON ", re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ' + i, line)[0])
        elif i.lower() in line:
            print("Line ", line_count, ": PERSON ", i.lower())



    for i in PRE_PERSON:  #Hata
        for j in re.findall(r'(?<= ' + i + ' )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*', line):
            print("Line ", line_count, ": PERSONxxx ", j)


    for i in MAN:
        for j in re.findall(i + r'\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]+', line):
            print("Line ", line_count, ": PERSON ", j)

    for i in WOMAN:
        for j in re.findall(i + r'\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]+', line):
            print("Line ", line_count, ": PERSON ", j)

    for i in ADJ_NOUN:
        for j in re.findall(r'(?<= ' + i + ' )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*', line):
            print("Line ", line_count, ": PERSON ", j)

        for j in re.findall( i.lower() , line):
            print("Line ", line_count, ": PERSON ", j)





    # Location
    for i in CITIES:
        if i in line:
            print("Line ", line_count, ": LOCATION ", i)

    for i in COUNTRIES:
        if i in line:
            print("Line ", line_count, ": LOCATION ", i)

    for i in CONTINENTS:
        if i in line:
            print("Line ", line_count, ": LOCATION ", i)

    for i in CAPITALS:
        if i in line:
            print("Line ", line_count, ": LOCATION ", i)

    # Organization
    for i in ORGANIZATION:
        if i in line:
            print("Line ", line_count, ": ORGANIZATION ", i)

    for i in POST_ORGANIZATIONS:
        for j in re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ' + i, line):
            print("Line ", line_count, ": ORGANIZATION ", j)

    for i in COMPANIES:
        if i in line:
            print("Line ", line_count, ": ORGANIZATION ", i)

    # Time
    for i in TIME:
        if i in line:
            print("Line ", line_count, ": TIME ", i)

    for i in MONTHS:
        if i in line:
            print("Line ", line_count, ": TIME ", i)

    for i in re.findall(r'[1-2][0-9]{3}[\'\"]da|[1-2]*[0-9]{3}[\'\"]de|[1-2]*[0-9]{3}[\'\"]te|[1-2]*[0-9]{3}[\'\"]ta', line):   #2023'te
        print("Line ", line_count, ": TIME ", i)

    for i in re.findall(r'[1-2][0-9][0-9][0-9] yılında', line):     # 2010 yılında
        print("Line ", line_count, ": TIME ", i)

    for i in MONTHS:
        for j in re.findall(r'([1-2]?[0-9]\s(?:' + i.capitalize() + '){0,1}(?=\'da))', line):  #10 Kasım'da
            print("Line ", line_count, ": TIME ", j)

    for i in MONTHS:
        for j in re.findall(r'([1-2]?[0-9]\s(?:' + i.capitalize() + '){0,1}(?=\'de))', line):
            print("Line ", line_count, ": TIME ", j)

    for i in MONTHS:
        for j in re.findall(r'([1-2]?[0-9]\s(?:' + i.capitalize() + '){0,1}(?=\'ta))', line):
            print("Line ", line_count, ": TIME ", j)

    for i in MONTHS:
        for j in re.findall(r'([1-2]?[0-9]\s(?:' + i.capitalize() + '){0,1}(?=\'te))', line):
            print("Line ", line_count, ": TIME ", j)

    for i in re.findall(r'[0-1][0-9][:.][0-5][0-9]|[2][0-9][:.][0-5][0-9]', line): #20:30 ya da 20.30
        print("Line ", line_count, ": TIME ", i)

    for i in re.findall(r'^\d{1,2}[\/.-]\d{1,2}[\/.-]\d{4}$', line):                #10/11/2020 ya da 10.11.2020 ya da 10-11-2020
        print("Line ", line_count, ": TIME ", i)





    for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*', line):
        uppercaseWord = line[uppercaseWord.start():uppercaseWord.end()]
        # print(uppercaseWord)
        # print("elma", uppercaseWord)
        if uppercaseWord.lower() in TIME:
            print("Line ", line_count, ": TIME ", uppercaseWord)

        if uppercaseWord.lower() in LOCATIONS:
            print("Line ", line_count, ": LOCATION ", uppercaseWord)



    line_count = line_count + 1  # Increase line count


