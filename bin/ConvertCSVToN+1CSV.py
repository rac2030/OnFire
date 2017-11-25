
delimeter = ";"
lines = []
maxLenth = 0;
with open('new300.csv') as f:
    for line in f:
        lines.append(line)
        arr = line.split(";")
        if(len(arr) > maxLenth):
            maxLenth = len(arr)
print(lines)
print(maxLenth)
fout = open("Tn+1.csv",encoding='utf8',mode='w')
newLine = ""
for line in lines:
    newLine = ""
    arr = line.split(delimeter)
    node = arr[len(arr) - 1]
    if(node.split("\n")):
        node = node.split("\n")[0]
    if(len(arr) - 1 > 0):
        for ctr in range(0, len(arr) - 1):
            newLine =  newLine + delimeter
    newLine = newLine + node
    for ctr in range(len(arr) - 1, maxLenth):
        newLine =  newLine + delimeter
    fout.write(newLine + '\n')

fout.close()
