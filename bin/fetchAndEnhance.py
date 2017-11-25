import urllib.request
import requests
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1, WatsonApiException
import watson_developer_cloud.natural_language_understanding.features.v1 as Features
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, \
    CategoriesOptions, ConceptsOptions, RelationsOptions

#inputurl = "https://hackathon17.mope.ml/HackathonSite/AccuracyTestNews300.txt"
#outputfile = 'AccuracyTestNews300.json'
inputurl = "https://hackathon17.mope.ml/HackathonSite/NewsAll.txt"
outputfile = 'NewsAllEnhanced.json'

news300 = urllib.request.urlopen(inputurl)
news300Bytes = news300.read()
news300String = news300Bytes.decode("utf8")
news300.close()

rawNewsRecords = news300String.split('\r\n\r\n')

records = []
for rawNewsRecord in rawNewsRecords:
    newsAttributes = rawNewsRecord.split('\r\n')
    newdict = {}
    for newsAttribute in newsAttributes:
        try:
            if not newsAttributes:
                break
            elements = newsAttribute.split(':', 1)
            if len(elements) < 2:
                break
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
data['data'] = records

nlu = NaturalLanguageUnderstandingV1(
    username="b6e37f9b-f1be-4fa9-9915-80e0333af98b",
    password="fR3R01sofxmU",
    version="2017-02-27")


def queryWatson(headline, story):
    return nlu.analyze(
        text=headline + "; " + story,
        language="en",
        features=Features(entities=EntitiesOptions(
            emotion=False, sentiment=False, limit=60),
            keywords=KeywordsOptions(
                emotion=False, sentiment=False, limit=60),
            categories=CategoriesOptions(limit=60),
            concepts=ConceptsOptions(limit=50)
        )
    )

try:
    for entry in data['data']:
        try:
            result = queryWatson(entry['headLine'], entry['headLine'])
            # enhance the entry
            entry['keywords'] = result['keywords']
            entry['entities'] = result['entities']
            entry['concepts'] = result['concepts']
            entry['categories'] = result['categories']
        except KeyError:
            print("KeyError with: " + json.dumps(result, indent=2))
        except WatsonApiException:
            print("API Exception: " + json.dumps(entry, indent=2))
        else:
            print(json.dumps(entry, indent=2))
finally:
    print("-------------- End result written to " + outputfile + " --------------")
    fout = open(outputfile,encoding='utf8',mode='w')
    fout.write(json.dumps(data, indent=2))
    fout.close()
