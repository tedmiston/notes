#!/bin/bash

# Print out the total number of lines of Markdown written.

line_count=$(find . -name '*.md' -print0 | xargs -0 wc -l | tail -n 1 | sed -e 's/total//' -e 's/ *//g')
echo $line_count "lines"
