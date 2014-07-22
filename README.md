Sample:
./send_feed.sh
[+] Feed: http://krebsonsecurity.com/feed/|[KerbsOnSecurity]
    -> Sending feed to: nrz@nullsecurity.net


Subject: [KerbsOnSecurity] http://krebsonsecurity.com/feed/
Body:
Even Script Kids Have a Right to Be Forgotten: http://krebsonsecurity.com/2014/07/even-script-kids-have-a-right-to-be-forgotten/

Indexeus, a new search engine that indexes user account information acquired from more than 100 recent data breaches, has caught many in the hacker underground off-guard. That's because the breached databases crawled by this search engine are mostly sites frequented by young ne'er-do-wells who are just getting their feet wet in the cybercrime business. [Fri, 18 Jul 2014 04:29:35 +0000]


Wireless Live CD Alternative: ZeusGard: http://krebsonsecurity.com/2014/07/wireless-live-cd-alternative-zeusgard/

I've long recommended that small business owners and others concerned about malware-driven bank account takeovers consider adopting a "Live CD" solution, which is a free and relatively easy way of temporarily converting your Windows PC into a Linux operating system. The trouble with many of these Live CD solutions is that they require a CD player (something many laptops no longer have) -- but more importantly - they don't play well with wireless access. Today's post looks at an alternative that addresses both of these issues. [Wed, 16 Jul 2014 04:00:20 +0000]


./send_feed.sh
[+] Feed: http://krebsonsecurity.com/feed/|[KerbsOnSecurity]
    -> Nothing new

Crontab:
00 */3 * * * /bin/bash /path_to/rss2mail/send_feed.sh &> /dev/null

Usage:
 - configure 'config.py'
 - configure 'send_mail.py' - 'smtp' and 'from' vars
 - Add rss to feeds.lst
 - Add recipients to mail_to.lst
 - Run send_feed.sh

Files:
 - send_feed.sh: main controller
 - rss_parser.py: output rss titles, urls and post date (depends: feedparser)
 - send_mail.py: send email with feeds
 - mail_to.lst: recipients for mailing
 - config.py: mail config
 - feeds.lst: feeds file - format: url_feed|mail_subject
