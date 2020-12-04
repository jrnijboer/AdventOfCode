def validatePassport(passports, check):
  a = 0
  for p in passports:
    valid = True
    if not "byr" in p or (check and not 1920 <= int(p["byr"]) <= 2002): valid = False
    if not "iyr" in p or (check and not 2010 <= int(p["iyr"]) <= 2020): valid = False
    if not "eyr" in p or (check and not 2020 <= int(p["eyr"]) <= 2030): valid = False
    if not "hgt" in p: valid = False
    elif check:        
        if p["hgt"].endswith("cm"):
          if not 150 <= int(p["hgt"][:-2]) <= 193: valid = False
        elif p["hgt"].endswith("in"):          
          if not 59 <= int(p["hgt"][:-2]) <= 76: valid = False
        else: valid = False
    if not "hcl" in p or (check and (p["hcl"][0] != "#" or len(p["hcl"]) != 7 or any([c not in "1234567890abcdef" for c in p["hcl"][1:]]))): valid = False
    if not "ecl" in p or (check and p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]): valid = False
    if not "pid" in p or (check and (len(p["pid"]) != 9 or any([c not in "1234567890" for c in p["pid"]]))): valid = False
    if valid: a += 1
  return a

input = [line.strip() for line in open("../input/day04.input").readlines()]
passports = []
passport = ""
for line in input:
    if len(line) > 0: passport += " " + line
    else:
        passportDict = {}
        kvps = passport[1:].split(" ")
        for kvp in kvps:
            s = kvp.split(":")
            passportDict[s[0]] = s[1]
        passports.append(passportDict)
        passport = ""

print("Answer A:", validatePassport(passports, False))
print("Answer B:", validatePassport(passports, True))
