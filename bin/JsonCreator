__author__ = 'F446178'
import json

def createJsonFromNewsFeed(filePath):
    newsJsonArray = {}
    inputFile = open(filePath, encoding="UTF-8")
    newsFile = inputFile.read()
    rawNewsRecords = newsFile.split("\n\n")
    ctr = 0
    for rawNews in rawNewsRecords:
        rawNewsAttributes = rawNews.split("\n")
        news = {}
        for attributes in rawNewsAttributes:
            if attributes.startswith('#### seqNo: '):
                news["seqNo"] = attributes.split('seqNo: ')[1]
            elif attributes.startswith("#### storyId: "):
                news["storyId"] = attributes.split("#### storyId: ")[1]
            if attributes.startswith("#### date: "):
                news["date"] = attributes.split("#### date: ")[1]
            elif attributes.startswith("#### headLine: "):
                news["headLine"] = attributes.split("#### headLine: ")[1]
            if attributes.startswith("#### topics: "):
                news["topics"] = attributes.split("#### topics: ")[1]
            elif attributes.startswith("#### topicsDescription: "):
                topicsDescription = attributes.split("#### topicsDescription: ")[1]
                topicsDescription = topicsDescription.replace('"', '')
                existingKeywordArray = topicsDescription.split(",")
                for keyword in existingKeywordArray:
                    print(keyword)
                    if keyword.startswith(" "):
                        keyword = keyword[1:]
                        print(keyword)
                news["topicsDescription"] = existingKeywordArray
            elif attributes.startswith("#### story: "):
                news["story"] = attributes.split("#### story: ")[1]

        newsJsonArray[ctr] = news
        ctr = ctr +1;
    print(newsJsonArray)
    mystring = str(newsJsonArray)

    print(newsJsonArray)

    jsonString = json.dumps(newsJsonArray)
    jsonObject = json.loads(jsonString)
    return  jsonObject

#test the method
json1 = createJsonFromNewsFeed("News300.txt")
print(json1['200']['story'])
#j = json.loads(news)
