"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""


f = open("input.txt")
blankTotal = 0
passports = []
passport = []

for l in f:
    if len(l) != 1:
        passport.append(l.strip())
    else:
        passports.append(passport)
        passport = []

tmpPassport = []
finalPassports = []

for passport in passports:
    for i in passport:
        if " " in i:
            
            