with open('in.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


class Passport:
    def __init__(self, byr=-1, iyr=-1, eyr=-1, hgt=-1, hfc=-1, ecl=-1, pid=-1, cid=-1):
        self.fields = {
            'byr': byr,
            'iyr': iyr,
            'eyr': eyr,
            'hgt': hgt,
            'hcl': hfc,
            'ecl': ecl,
            'pid': pid,
            'cid': cid,
        }


def parse(line):
    fields = line.split()
    dd = {}
    for field in fields:
        key1, value1 = field.split(':')
        dd[key1] = value1
    return dd


passport_list = []
counter = 0
passport = Passport()

for line in lines:
    line = line.strip()
    if len(line) == 0:
        for key, value in passport.fields.items():
            if key != 'cid' and value == -1:
                counter += 1
                break
            # -------- TASK 2 CONDITIONS ---------
            if key == 'byr' and (int(value) < 1920 or int(value) > 2002):
                counter += 1
                break
            if key == 'iyr' and (int(value) < 2010 or int(value) > 2020):
                counter += 1
                break
            if key == 'eyr' and (int(value) < 2020 or int(value) > 2030):
                counter += 1
                break
            if key == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        counter += 1
                        break
                elif value[-2:] == 'in':
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        counter += 1
                        break
                else:
                    counter += 1
                    break
            if key == 'hcl':
                if value[0] != '#':
                    counter += 1
                    break
                value = value[1:]
                if len(value) != 6:
                    counter += 1
                    break
            if key == 'ecl':
                if value not in ('amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth'):
                    counter += 1
                    break
            if key == 'pid':
                if len(value) != 9:
                    counter += 1
                    break
            # ----------------------------
        passport_list.append(passport)
        passport = Passport()
    d = parse(line)
    for key, value in d.items():
        passport.fields[key] = value


print(len(passport_list) - counter)
