Sample Script:
==============

    ./rss2mail.sh
    [+] Feed: http://www.reddit.com/r/ReverseEngineering|[reddit][ReverseEngineering]
        -> Sending feed to: nrz@nullsecurity.net
    [+] Feed: http://www.reddit.com/r/netsec|[reddit][netsec]
        -> Nothing new

Sample Mail:
============
    Subject: [reddit][ReverseEngineering] http://www.reddit.com/r/ReverseEngineering
    Body:
    Detouring register values in a x86 asm (c++, dll injection):
    http://www.reddit.com/r/ReverseEngineering/comments/2bfb5w/detouring_register_values_in_a_x86_asm_c_dll/

    Hi everyone, I was wondering if you would mind taking a look at the problem I posted on stackoverflow: http://stackoverflow.com/questions/24896388/get-register-value-by-detouring-specific-address-x86-assembly-on-windows As the title says, I'm trying to detour the register value and put it into my variable in c++. I think the post is well explained, but you can ask if you have any questions! Your community have been helpful in the past so I'm taking a chance here, hope I don't bother anyone with my questions!   submitted by  5tapler   [link] [6 comments]
    [Tue, 22 Jul 2014 19:50:34 +0000]

Crontab:
========
    00 */3 * * * /bin/bash /path_to/rss2mail/rss2mail.sh &> /dev/null

Usage:
======
 - configure 'config.py'
 - Add rss to feeds.lst
 - Add recipients to mail_to.lst
 - Run rss2mail.sh

Files:
======
 - rss2mail.sh: main controller
 - rss_parser.py: output rss titles, urls and feed date (depends: feedparser)
 - send_mail.py: send email with feeds
 - mail_to.lst: recipients for mailing
 - config.py: mail config
 - feeds.lst: feeds file - format: url_feed|mail_subject
