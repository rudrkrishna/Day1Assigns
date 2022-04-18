#Return all the duplicate values from list of arraylist

from collections import Counter

li=[[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

for i in range(0, len(li)):
    duplDict={}
    for j in range(0, len(li[i])):
        k = j + 1
        for l in range(k, len(li[i])):
            if li[i][j] == li[i][l] and li[i][j] not in duplDict:
                duplDict[li[i][j]]=li[i].count(li[i][j])
    print(duplDict)

#Merge two lists

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[]

for i in range(0, len(list1)):
    for j in range(0, len(list2)):
        list3.append(" ".join([list1[i], list2[j]]))
print(list3)


#Map Dictionary

Keys = ["Ten", "Twenty", "Thirty"]
Value = [10, 20, 30]
dictTemp={}
for i in range(0, len(Keys)):
    dictTemp[Keys[i]] = Value[i]
print(dictTemp)

#Merge two dictionaries

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

#Rename Key city to Location

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict["location"]=sampleDict.pop("city")
print(sampleDict)


#convert dictionary to list

dict = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
dictlist=[]

for key, value in dict.items():
    temp = []
    temp.append(key)
    for k in range(0, len(value)):
        temp.append(value[k])
    dictlist.append(temp)
print(dictlist)

