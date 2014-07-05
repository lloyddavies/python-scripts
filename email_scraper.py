#!/usr/bin/python

import sys
import urllib
import re

email_regex = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

def main():
    url = sys.argv[1]
    content = urllib.urlopen(url)
    info = content.info()
    assert info.gettype() == 'text/html', 'Content not of type text/html'
    text = content.read()
    emails = set(re.findall(email_regex, text, re.IGNORECASE))
    for email in emails:
        print email

if __name__ == '__main__':
    main()
