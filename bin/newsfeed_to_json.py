import json
inputfile = 'basedata/News300.txt'
outputfile = 'basedata/News300.json'
fin = open(inputfile,encoding='utf8')
fout = open(outputfile,encoding='utf8',mode='w')

instream = fin.read()

rawNewsRecords = instream.split('\n\n')

records = []
for rawNewsRecord in rawNewsRecords:
    newsAttributes = rawNewsRecord.split('\n')
    newdict = {}
    for newsAttribute in newsAttributes:
        try:
            elements = newsAttribute.split(':', 1)
            elements[0] = elements[0].replace('#### ', '')
            elements[1] = elements[1].replace('"', '')
            splited_values = elements[1].split(',')

            if elements[0] in ['seqNo', 'storyId', 'headLine', 'story']:
                newdict[elements[0]] = elements[1]
            else:
                newdict[elements[0]] = splited_values
        except Exception as inst:
            print(inst)
    records.append(newdict)

data = {}
data['data']=records

fout.write(json.dumps(data))
fout.close()
