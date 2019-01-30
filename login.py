#!/usr/bin/env python3

import cgi, cgitb # enable debugging with HTML code output 
cgitb.enable()
import sys, codecs 
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # UTF-8 encoding for print statements 

form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8")
print("\n\n")  # double line break for header separation 

import pymysql.cursors

from string import Template

a = open(r"web_quiz_template_1.txt")
template = Template(a.read())
subs = {'title':'Database Design'}
html_output = template.substitute(subs)
print(html_output)