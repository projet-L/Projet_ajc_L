#!/usr/bin/env python
# coding:utf-8

import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import requests



# account credentials
username = "ProjetL.formation@gmail.com"
password = "5-Formation"

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)
    

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 3
# total number of emails
messages = int(messages[0])
sub=[]

def subject_find():

    for i in range(messages, messages-N, -1):
    # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                    # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
		    
                if subject[0:7]=="[FIRING":
                    #print("Subject:", subject)
                    #print("From:", From)
                    sub.append(subject)
                    #print(sub)
                    #print("="*100)
	# close the connection and logout
    imap.close()
    imap.logout()
    return sub
subject_find()
print(sub)

    

