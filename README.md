Sample Script:
==============

    ./rss2mail.sh
    [+] Feed: http://www.reddit.com/r/ReverseEngineering|[reddit][RE]
        -> Sending feed to: nrz@nullsecurity.net
    [+] Feed: http://krebsonsecurity.com/feed/|[KerbsOnSecurity]
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

    Subject: [KerbsOnSecurity] http://krebsonsecurity.com/feed/
    Body:
    Even Script Kids Have a Right to Be Forgotten: http://krebsonsecurity.com/2014/07/even-script-kids-have-a-right-to-be-forgotten/

    Indexeus, a new search engine that indexes user account information acquired from more than 100 recent data breaches, has caught many in the hacker underground off-guard. That's because the breached databases crawled by this search engine are mostly sites frequented by young ne'er-do-wells who are just getting their feet wet in the cybercrime business.
    [Fri, 18 Jul 2014 04:29:35 +0000]


    Wireless Live CD Alternative: ZeusGard: http://krebsonsecurity.com/2014/07/wireless-live-cd-alternative-zeusgard/

    I've long recommended that small business owners and others concerned about malware-driven bank account takeovers consider adopting a "Live CD" solution, which is a free and relatively easy way of temporarily converting your Windows PC into a Linux operating system. The trouble with many of these Live CD solutions is that they require a CD player (something many laptops no longer have) -- but more importantly - they don't play well with wireless access. Today's post looks at an alternative that addresses both of these issues. 
    [Wed, 16 Jul 2014 04:00:20 +0000]

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
