def minion_game(string):
    isVowel = lambda x: x in 'AEIOU'
    stuartScore = 0
    kevinScore = 0
    stuartSubStrings = {}
    kevinSubStrings = {}

    i = 0
    end = len(string)
    start = 0
    for c in string:
        if (isVowel(c)):
            scoreDict = kevinSubStrings
        else:
            scoreDict = stuartSubStrings
        j = start + 1
        while (j <= end):
            subStr = string[start:j]
            if subStr not in scoreDict:
                scoreDict[subStr] = 0
            scoreDict[subStr] += 1
            j += 1
        start += 1 

    for k in stuartSubStrings.keys():
        stuartScore += stuartSubStrings[k]
    for k in kevinSubStrings.keys():
        kevinScore += kevinSubStrings[k]
    
    if (kevinScore > stuartScore):
        print("Kevin", kevinScore)
    elif (kevinScore < stuartScore):
        print("Stuart", stuartScore)
    else:
        print("Draw")

if __name__ == '__main__':
    minion_game("BANANANAAAS")