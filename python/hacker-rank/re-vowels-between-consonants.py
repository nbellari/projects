import re

if __name__ == "__main__":
    vowels = "aeiou"
    consonants = "qwrtypsdfghjklzxcvbnm"

    str = input().strip()

    match_set = re.findall(r'[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', str, re.IGNORECASE)
    if match_set:
        for m in match_set:
            print(m)
    else:
        print(-1)

        re.DEBUG
