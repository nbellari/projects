def minion_game(string):
    isVowel = lambda x: x in 'AEIOU'
    stuartScore = 0
    kevinScore = 0

    end = len(string)

    i = 0    
    for s in string:
        if (isVowel(s)):
            kevinScore += (end - i)
        else:
            stuartScore += (end - i)
        i += 1

    if (kevinScore > stuartScore):
        print("Kevin", kevinScore)
    elif (kevinScore < stuartScore):
        print("Stuart", stuartScore)
    else:
        print("Draw")

if __name__ == '__main__':
    minion_game("BANANA")