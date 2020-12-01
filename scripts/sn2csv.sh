#!/bin/bash

if [[ $# -ne 3 ]];
then
    echo "Usage: sn2csv.sh <file> <Title> <Author>"
    echo "        A file containing highlights from sumnotes.net"
    echo "        Title of the document/article/book"
    echo "        Author of the document/article/book"
    exit
fi

inputFile=$1
title=$2
author=$3

#echo "Title: $title"
#echo "Author: $author"

# A series of transformations on the file follows

# 1. Remove empty lines
sed -i '/^$/d' $inputFile

# 2. Remove "Page" lines from the file
sed -i '/^Page/d' $inputFile

#3. Remove any quotes from the text
sed -i 's/"//g' $inputFile

# 3. Add quotes to each line
sed -i 's/^/"/;s/$/"/' $inputFile

# 4. Add Title and author to each line
sed -i "s/$/,\"$title\",\"$author\"/" $inputFile

# 5. Add header to the file
sed -i '1i Highlight,Title,Author,URL,Note,Location' $inputFile

