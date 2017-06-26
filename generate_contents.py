#!/usr/bin/env python3

"""
Converted a tab-indented input file of chapters > sections > subsections, etc
into a Markdown hierarchy.

Usage:

- Populate a file "in.txt" like sample input below
- Run it
- Use redirection to write to an output file instead of the shell

Input:

    # My Book Title

    Introduction
    Chapter 1
        Section 1.1
            Section 1.1.1
        Section 1.2
    Chapter 2
        Section 2.1
    Conclusion

Output:

    # My Book Title

    ## Introduction

    ## Chapter 1
    ### Section 1.1
    #### Section 1.1.1
    ### Section 1.2

    ## Chapter 2
    ### Section 2.1

    ## Conclusion
"""

import re


def load_file(filename):
    """Load the contents of an input file."""
    try:
        with open(filename) as fp:
            # no lstrip() because leading indentation is significant
            text = fp.read().rstrip()
    except FileNotFoundError as e:
        exit('Error: Input file "{}" does not exist.'.format(filename))

    if text == '':
        exit('Error: Input file "{}" is blank.'.format(filename))

    return text.split(sep='\n')


def parse_title(lines):
    """Parse book title (optional)."""
    TITLE_PREFIX = '# '
    book_title = None
    if lines[0].startswith(TITLE_PREFIX):
        book_title = lines.pop(0)[len(TITLE_PREFIX):].strip()
    return book_title


def parse_chapters(lines):
    """Parse chapter titles and depth level."""
    chapters = []
    for chapter in lines:
        depth = len(re.findall(r' {4}|\t', chapter))
        title = chapter.strip()
        if len(title) != 0:
            chapters.append((title, depth))
    return chapters


def parse(lines):
    """Parse the lines of an input file."""
    title = parse_title(lines)
    chapters = parse_chapters(lines)
    return title, chapters


def serialize_heading(title, depth):
    """Generate h1-h6 in Markdown."""
    return '{} {}'.format('#' * depth, title)


def serialize_chapters(chapters):
    """Generate Markdown for chapters."""
    markdown_chapters = []
    for title, indent in chapters:
        markdown_chapter = serialize_heading(title, depth=indent+2)
        if indent == 0:
            markdown_chapter = '\n' + markdown_chapter
        markdown_chapters.append(markdown_chapter)
    return markdown_chapters


def serialize_title(title):
    """Generate Markdown for title."""
    return serialize_heading(title, depth=1) if title is not None else ''


def serialize(title, chapters):
    """Generate the Markdown components and combine them."""
    chapters_md = serialize_chapters(chapters)
    title_md = serialize_title(title)
    return '\n'.join([title_md] + chapters_md).strip()


def main():
    """Convert tab tree contents to Markdown contents."""
    lines = load_file('in.txt')
    output = serialize(*parse(lines))
    print(output)


if __name__ == '__main__':
    main()
