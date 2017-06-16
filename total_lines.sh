#!/bin/bash

# Print total line count and word count of all notes.

line_count=$(find . -name '*.md' -print0 | xargs -0 wc -l | tail -n 1 | sed -e 's/total//' -e 's/ *//g')
word_count=$(find . -name '*.md' -print0 | xargs -0 wc -w | tail -n 1 | sed -e 's/total//' -e 's/ *//g')

echo $line_count "lines"
echo $word_count "words"
