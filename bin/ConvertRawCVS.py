import  os

n0 = 'Reuters News Topics'
n1 = ''
n2 = ''
n3 = ''
n4 = ''
n5 = ''
n6 = ''
delimeter = ";"

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

fout = open("new300.csv",encoding='utf8',mode='w')

with open('T0.CSV') as f:
    for line in f:
        newline = ''
        if line.startswith(';;;;;;'):
            n6 = find_between(line, ";;;;;;", ";")
            newline = n0 + delimeter + n1 + delimeter + n2 + delimeter + n3 + delimeter +  n4 + delimeter + n5 + delimeter + n6
            print(newline)
        elif line.startswith(';;;;;'):
            n5 = find_between(line, ";;;;;", ";;")
            newline = n0 + delimeter + n1 + delimeter + n2 + delimeter + n3 + delimeter +  n4 + delimeter + n5
            print(newline)
        elif line.startswith(';;;;'):
            n4 = find_between(line, ";;;;", ";;;")
            newline = n0 + delimeter + n1 + delimeter + n2 + delimeter + n3 + delimeter + n4
            print(newline)
        elif line.startswith(';;;'):
            n3 = find_between(line, ";;;", ";;;;")
            newline = n0 + delimeter + n1 + delimeter + n2 + delimeter + n3
            print(newline)
        elif line.startswith(';;'):
            n2 = find_between(line, ";;", ";;;;;")
            newline = n0 + delimeter + n1 + delimeter + n2
            print(newline)
        elif line.startswith(';'):
            n1 = find_between(line, ";", ";;;;;;")
            newline = n0 + delimeter + n1
            print(newline)
        fout.write(newline + '\n')
fout.close()
