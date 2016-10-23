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

Note: Python 3
"""

import re


def generate_heading(title, depth):
    """Generate h1-h6 in Markdown."""
    return '{} {}'.format('#' * depth, title)


def parse_title(chapters_input):
    """Parse book title (optional)."""
    book_title = None
    if chapters_input[0].startswith('# '):
        book_title = chapters_input.pop(0)[2:].strip()
    return book_title


def parse_chapters(chapters_input):
    """Parse chapter titles and depth level."""
    chapters = []
    for chapter in chapters_input:
        depth = len(re.findall(r'    |\t', chapter))
        title = chapter.strip()
        if len(title) != 0:
            chapters.append((title, depth))
    return chapters


def generate_chapters(chapters):
    """Generate Markdown for chapters."""
    markdown_chapters = []
    for title, indent in chapters:
        markdown_chapter = generate_heading(title, depth=indent+2)
        if indent == 0:
            markdown_chapter = '\n' + markdown_chapter
        markdown_chapters.append(markdown_chapter)
    return markdown_chapters


def generate_title(title):
    """Generate Markdown for title."""
    return generate_heading(title, depth=1) if title is not None else ''


def generate_markdown(title, chapters):
    """Generate the Markdown components and combine them."""
    chapters_md = generate_chapters(chapters)
    title_md = generate_title(title)

    everything_md = '\n'.join([title_md] + chapters_md).strip()
    return everything_md


def main():
    """Convert tab tree contents to Markdown contents."""
    INPUT_FILE = 'in.txt'

    try:
        with open(INPUT_FILE) as fp:
            text = fp.read().strip()
    except FileNotFoundError as e:
        exit('Error: Input file "{}" does not exist.'.format(INPUT_FILE))

    if text == '':
        exit('Error: Input file "{}" is blank.'.format(INPUT_FILE))

    chapters_input = text.split(sep='\n')

    title = parse_title(chapters_input)
    chapters = parse_chapters(chapters_input)

    output = generate_markdown(title, chapters)
    print(output)


if __name__ == '__main__':
    main()
