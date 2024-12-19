# take in an array of chars
def decomposeWord(jword):
#  word2 = [*jword]
  for char in jword:
    print(char)
    print(findRadicals(char))

# remove duplicates from kanji and return array of unique
def getUniqueWordKanji(word):
  testwordchar = [*word]
  uniquechar = set(testwordchar)
  return uniquechar

# print radicals per kanji
def printRadicalsPerWordInList(wordList):
  for w in wordList:
    print("-----" + w + "-----")
    decomposeWord(getUniqueWordKanji(w))

# unnecessary - remove
def findInDic(kanji, dict):
  if kanji in dict:
      dict[kanji]['count'] += 1
      #print(kanji)
      #print(dict[kanji])

# unnecessary - remove
def countKanjiAppearance(list1, thedic):
  for num in createKanjiNumber(list1):
    #print(num)
    findInDic(num, thedic)

def createKanjiNumber(thelist):
  templ = []
  for word in thelist:
    for z in [*word]:
      templ.append(z)
  return set(templ)