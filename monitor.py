#!/usr/bin/env python
# coding:utf-8

import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import requests
import jenkins
import time

#jenkins login

JENKINS_URL = "http://localhost:8080"
JENKINS_USERNAME = "admin"
JENKINS_PASSWORD = "admin"

# account credentials
username = "ProjetL.formation@gmail.com"
password = "5-Formation"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 3
# total number of emails
messages = int(messages[0])
print(messages)
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
    


    
def build_job(name, parameters=None, token=None):
    jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
    next_build_number = jenkins_server.get_job_info(name)['nextBuildNumber']
    jenkins_server.build_job(name, parameters=parameters, token=token)
    time.sleep(10)
    build_info = jenkins_server.get_build_info(name, next_build_number)
    return build_info








subject_find()

if len(sub)==0:
    print("no new mail")
    quit()
for i in range(len(sub)):
    alert=sub[i]

    """
    if alert[0:7]=="[FIRING":
        NAME_OF_JOB = "test"
        TOKEN_NAME = "bob"
        # Example Parameter
        PARAMETERS = None
    """
    if alert[-3:]=="xy)":
        NAME_OF_JOB = "test"
        TOKEN_NAME = "bob"
        # Example Parameter
        PARAMETERS = None
    output = build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    print ("Jenkins Build URL: {}".format(output['url']))

    

