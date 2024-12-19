import json

class KanjiRad:
  def __init__(self, name, radicals):
    self.name = name
    self.radicals = radicals

karray = []
mylist = ['経験経験', '巡る', '楽器', '火曜日', '火災', '火山']

# ------- BEGIN FILE OPERATIONS -------

with open("test.txt", "r") as file:
  for line in file:
    kanji = line.split(":")[0].replace(" ","")
    radicals = list(filter(None, (line.split(":")[1].strip().split(" "))))
    dict = {'name': kanji, 'rads': radicals}
    karray.append(dict)
  file.close()

with open("mydata.json", "w") as final:
  json.dump(karray, final)
  final.close()

# Opening JSON file
f = open('mydata.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# ------- BEGIN RADICAL FUNCTIONS  -------
def findRadicals(kanji):
  for member in data:
    if member['name'] == kanji:
      if list(member['rads']) is None:
        return []
      else:
        return list(member['rads'])
  return []

def totalUniqueRadicals(wordList):
  templ = []
  for word in wordList:
    for z in [*word]:
      templ = templ + findRadicals(z)
    # unique list of radicals in words
  return set(templ)

def makeRadicalDictionary(wordList):
  countlist = []
  uniquekanji = totalUniqueRadicals(wordList)
  for r in uniquekanji:
    countlist.append({ r: {'count' : 0 , 'words': []}})
  kanji_dict = {list(d.keys())[0]: list(d.values())[0] for d in countlist}
  return kanji_dict

def getRadicalCountAndWords(wordList):
  print("---------------------------------------")
  #step 1: create the dictionary
  dict = makeRadicalDictionary(wordList)
  # step 2: go through words. if word contains the kanji, add to dict words
  for word in wordList:
    components = [*word]
    uniqueComponents = set(components)
    for component in uniqueComponents:
      for radical in findRadicals(component):
        if radical in dict and word not in dict[radical]['words']:
          dict[radical]['words'].append(word)
          # print("true")
          # print(radical, word)
          # print(dict[radical])
  return dict

# ------- BEGIN KANJI FUNCTIONS -------

def totalUniqueKanji(wordList):
  templ = []
  for word in wordList:
    for z in [*word]:
      templ.append(z)
    # unique list of kanji in words
  return set(templ)

def makeKanjiDictionary(wordList):
  countlist = []
  uniquekanji = totalUniqueKanji(wordList)
  for k in uniquekanji:
    countlist.append({ k: {'count' : 0 , 'words': []}})
  kanji_dict = {list(d.keys())[0]: list(d.values())[0] for d in countlist}
  return kanji_dict

def getKanjiCountAndWords(wordList):
  print("---------------------------------------")
  #step 1: create the dictionary
  dict = makeKanjiDictionary(wordList)
  # step 2: go through words. if word contains the kanji, add to dict words
  for word in wordList:
    components = [*word]
    uniqueComponents = set(components)
    for component in uniqueComponents:
      if component in dict:
        dict[component]['words'].append(word)
        print("true")
        print(component, word)
        print(dict[component])
  return dict

# ------- RUN FUNCTIONS HERE -------

print(getRadicalCountAndWords(mylist))