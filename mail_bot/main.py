import imaplib
import email
from email.header import decode_header
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
# imap.search(None, 'ALL').index()[-1]

# количество популярных писем для получения
N = 1
# общее количество писем
messages = int(messages[0])
for i in range(messages, messages - N, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    msg = email.message_from_bytes(msg[0][1])
    letter_id = msg["Message-ID"]  # айди письма
    letter_from = msg["Return-path"]  # e-mail отправителя
    msg_head = decode_header(msg["Subject"])[0][0].decode()
    x = msg_head.split()
    print(x)
    for i in msg_head:
        if i == 'Звальненне':
            print(msg_head)
    # for i in x:
    #     if i == 'Звільнення':
    #         print(msg_head)
    # for i in x:
    #     if i == 'Увольнение':
    #         print(msg_head)
# print(msg_head, "It's work!")
# for part in msg.walk():
#     if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
#         print(base64.b64decode(part.get_payload()).decode())
