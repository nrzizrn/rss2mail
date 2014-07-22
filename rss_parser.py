#!/usr/bin/env python

# author: nrz@nullsecurity.net

import feedparser
import sys
import re
import hashlib

TAG_RE = re.compile(r'<[^>]+>')

def usage():
    print "get_rss_feed.py <url> <file_done>"

def md5_text(text):
    m = hashlib.md5()
    m.update(text)
    return m.hexdigest()

def remove_tags(text):
    return TAG_RE.sub('', text)

def already_sended(title, file_done):
    ret = False
    try:
        file = open(file_done, "r")
    except:
        # file doesnt exist yet
        return False
    for line in file:
        if str(md5_text(title)) == line.rstrip('\n'):
            ret = True
    return ret

def save_title(title, file_done):
    f = open(file_done,'a+')
    f.write(md5_text(title) + '\n') # python will convert \n to os.linesep
    f.close()


def main():

    try:
        if len(sys.argv) != 3:
            raise
        url = sys.argv[1]
        file_done = sys.argv[2]
    except:
        usage()
        sys.exit(1)

    d = feedparser.parse(url)

    for post in d.entries:

        title = post.title.encode('utf-8')

        if already_sended(title, file_done):
            continue

        save_title(title, file_done)
        link = post.link.encode('utf-8')
        summary = remove_tags(post.summary.encode('utf-8'))

        try:
            published = post.published.encode('utf-8')
        except:
            published = ''

        print title + ": " + link + "\n\n" + summary \
                + " [" + published + "]\n\n\n"

main()
