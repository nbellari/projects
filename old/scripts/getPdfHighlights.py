#!/usr/bin/python3

# In case the script is manually invoked with python, check version
import sys
import fitz

if (sys.version_info.major != 3):
    print("Use python3 to run this script!")
    sys.exit(1)

if (len(sys.argv) != 2):
    print("Usage: {} <file>".format(sys.argv[0]))
    sys.exit(1)

file = sys.argv[1]

try:
    doc = fitz.open(file)
except:
    print ("Failed to open {}".format(file))
    sys.exit(1)

print("Opened {} with {} pages".format(file, len(doc)))


highlight_text = []
for page in doc:
    # list to store the co-ordinates of all highlights
    highlights = []

    # loop till we have highlight annotation in the page
    annot = page.firstAnnot
    while annot:
        if annot.type[0] == 8:
            all_coordinates = annot.vertices
            if len(all_coordinates) == 4:
                highlight_coord = fitz.Quad(all_coordinates).rect
                highlights.append(highlight_coord)
            else:
                all_coordinates = [all_coordinates[x:x+4] for x in range(0, len(all_coordinates), 4)]
                for i in range(0,len(all_coordinates)):
                    coord = fitz.Quad(all_coordinates[i]).rect
                    highlights.append(coord)
        annot = annot.next

    all_words = page.getTextWords()

    # List to store all the highlighted texts
    for h in highlights:
        sentence = [w[4] for w in all_words if   fitz.Rect(w[0:4]).intersect(h)]
        highlight_text.append(" ".join(sentence))

# Cleanup the list by hyphenated sentences
line = 0
while (line < len(highlight_text)-1):
    if (highlight_text[line][len(highlight_text[line])-1] == "-"):
        highlight_text[line] = highlight_text[line][:-1] + highlight_text[line+1]
        highlight_text.remove(highlight_text[line+1])
        continue
    line += 1

print ("Collected {} highlights".format(len(highlight_text)))

file = open("highlights.txt", "w")
for h in highlight_text:
    file.write(h)
    file.write("\n")
file.close()

print ("Wrote {} highlights to highlight.txt".format(len(highlight_text)))
