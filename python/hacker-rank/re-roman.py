import re

if __name__ == "__main__":
    str = input().strip()
    match = re.search(r'[IVXLCDM]+', str)
    if match:
        print("1 - " + match.group())
    
    match = re.search(r'([IXCM]{0,3})*', str, re.VERBOSE)
    if match:
        print("2 - " + match.group(0))
    
    match = re.search(r'[VLD]{0,1}', str)
    if match:
        print("3 - " + match.group())
    
    match = re.search(r'I[^CDML]', str)
    if match:
        print("4 - " + match.group())
    
    match = re.search(r'X[^DM]', str)
    if match:
        print("5 - " + match.group())
