#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    stack = []
    if(html == ''):
        return True
    if(len(_extract_tags(html)) == 0):
        return False
    for tag in _extract_tags(html):
        if tag[1] != '/':
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1][1:-1] == tag[2:-1]:
                    stack.pop()
    return len(stack) == 0

    # HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm
    # from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be
    used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the
    input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tag = ''
    tags = []
    for char in html:
        if char in '<':
            tag += char
        else:
            if len(tag):
                if char in '>':
                    tag += char
                    tag = valid_html_tag(tag)
                    tags.append(tag)
                    tag = ''
                else:
                    tag += char
    return tags


def valid_html_tag(tag):
    '''
    This is a function for validating if a tag contains a default html tag
    and modify if necessary
    >>> valid_html_tag('')
    ''
    >>> valid_html_tag('<strong test>')
    '<strong>'
    '''
    default_tags = ['<strong', '</strong', '<a', '</a', '<span', '</span']
    for default_tag in default_tags:
        if default_tag in tag:
            return default_tag + '>'
    return tag
