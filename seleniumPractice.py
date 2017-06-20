#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:18:52 2017

@author: mmonforte
"""

from selenium import webdriver
import time, credentials
browser = webdriver.Chrome()
browser.get('http://gmail.com')

try:
    """
    # This section was to test identification of element names.    
    browser.get('http://gmail.com')
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
    """
    
    """
    # This section was testing page clicks.
    browser.get('http://gmail.com')
    linkElem = browser.find_element_by_link_text('Read It Online')
    linkElem.click()
    """
    
    # This section is testing forms, clicks, and submissions.
    waitTime = 2
    
    browser.get('http://gmail.com')
    time.sleep(waitTime)
    
    emailElem = browser.find_element_by_id('identifierId')
    emailElem.send_keys(credentials.gmail_username)
    time.sleep(waitTime)
    
    nextButtonElem = browser.find_element_by_id('identifierNext')
    nextButtonElem.click()
    time.sleep(waitTime)
    
    passwordElem = browser.find_element_by_name('password')
    passwordElem.send_keys(credentials.gmail_password)
    time.sleep(waitTime)
    
    passwordButton = browser.find_element_by_id('passwordNext')
    passwordButton.click()
    
except:
    print('Request failed.')