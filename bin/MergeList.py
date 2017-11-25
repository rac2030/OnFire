
originalList = ["Reuters News Topics", "Reuters News Topics;News Topics", "Reuters News Topics;News Topics;General News Topics"]
newsList = []

str1 = "Reuters News Topics;News Topics"
str2 = "Reuters News Topics;News Topics;NewNode"


for line in originalList:
    if(line is str1):
        newsList.append(line)
        newsList.append(str2)
    else:
        newsList.append(line)

print(newsList)
