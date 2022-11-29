import imaplib
import email
from email.header import decode_header
import json
import base64

import ppprint as ppprint
from bs4 import BeautifulSoup
import re

mail_pass = "SSghkvsBXWrgs0isJtUQ"
username = "e.shantrukov@ydt-global.com"
imap_server = "imap.mail.ru"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)
status, messages = imap.select("INBOX")
dismissal_dict = {}

messages = int(messages[0])
N = messages

for i in range(messages, messages -N, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    msg = email.message_from_bytes(msg[0][1])
    letter_id = msg["Message-ID"]  # айди письма
    letter_from = msg["Return-path"]  # e-mail отправителя
    msg_head = decode_header(msg["Subject"])[0][0].decode()
    x = msg_head.split()
    k = 1
    for t in x:
        if t == 'Звальненне':
            q = msg_head
            for b in t:
                dismissal_dict[k] = {
                    "dismissal_title": q
                }
                k += 1
            with open("dismissal_dict.json", "w") as file:
                    json.dump(dismissal_dict, file, indent=1, sort_keys=True, ensure_ascii=False)
    # for i in x:
    #     if i == 'Звільнення':
    #         print(msg_head)
    # for i in x:
    #     if i == 'Увольнение':
    #         print(msg_head)
