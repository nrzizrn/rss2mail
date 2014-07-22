#!/bin/bash

# author: nrz@nullsecurty.net

path="path_to/rss2mail"

while read -r feed; do
    printf "[+] Feed: %s\n" "${feed}"
    rss="$(printf "${feed}"|cut -d"|" -f1)"
    subject="$(printf "${feed}"|cut -d"|" -f2) ${rss}"
    # file to store feeds alread sended
    file_done="${path}/done/$(printf ${rss}|sed 's?http:??;s?/??g').done"
    parser_output="$(python ${path}/rss_parser.py ${rss} ${file_done})"
    # if has nothing to send dont send it
    [ "${parser_output}" == '' ] && printf "    -> Nothing new\n" && continue
    while read to; do
        printf "    -> Sending feed to: %s\n" "${to}"
        python "${path}/send_mail.py" "${subject}" "${parser_output}" "${to}" &> /dev/null
    done < "${path}/mail_to.lst"
done < "${path}/feeds.lst"

