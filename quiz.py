#!/usr/bin/env python3

import cgi, cgitb # enable debugging with HTML code output 
cgitb.enable()
import sys, codecs 
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # UTF-8 encoding for print statements 

form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8")
print("\n\n")  # double line break for header separation 

import pymysql.cursors
z = 0
nameInsert = form.getvalue('name')
mailInsert = form.getvalue('mail')
x = 0
q1 = form.getvalue('q1'); q1a = "2007"
if q1 == q1a:
  x += 10;
q2 = form.getvalue('q2'); q2a = "South Korea"
if q2 == q2a:
  x += 10;
q3 = form.getvalue('q3'); q3a = "1959"
if q3 == q3a:
  x += 10;
q4 = form.getvalue('q4'); q4a = "High Sierra"
if q4 == q4a:
  x += 10;
q5 = form.getvalue('q5'); q5a = "Canberra"
if q5 == q5a:
  x += 10;
q6 = form.getvalue('q6'); q6a = "Mikhail Gorbachev"
if q6 == q6a:
  x += 10
q7 = form.getvalue('q7'); q7a = "54.6 Million km"
if q7 == q7a:
  x += 10
q8 = form.getvalue('q8'); q8a = "1977"
if q8 == q8a:
  x += 10
q9 = form.getvalue('q9'); q9a = "Edward Hopper"
if q9 == q9a:
  x += 10
q10 = form.getvalue('q10'); q10a = "5"
if q10 == q10a:
  x += 10

from string import Template

connection = pymysql.connect(host='warehouse.cims.nyu.edu',
  user='******',
  passwd='********',
  db='******_db_1',
  charset = 'utf8mb4',
  cursorclass=pymysql.cursors.DictCursor) 

stmt = (""" SELECT * FROM quiz WHERE name = %s AND email = %s """)
data = (nameInsert, mailInsert)

stmt2 = (""" INSERT INTO quiz (name, email) VALUES (%s,%s) """)
data2 = (nameInsert, mailInsert)

stmt3 = (""" UPDATE quiz SET q1=%s,q2=%s,q3=%s,q4=%s,q5=%s,q6=%s,q7=%s,q8=%s,q9=%s,q10=%s,correct=%s ORDER BY id DESC LIMIT 1 """)
data3 = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, x)

stmt4 = (""" SELECT correct FROM quiz WHERE name = %s and email = %s """)
data4 = (nameInsert, mailInsert)

cxn = connection.cursor()

cxn.execute(stmt,data)

results = cxn.fetchall()
count = cxn.rowcount

#print(mailInsert)
#print(nameInsert)
#print(count)

for row in results:
  if row['name'] == nameInsert and row['email'] == mailInsert: # if user already in database, output results 
    a = open(r"results.txt")
    template = Template(a.read())
    cxn.execute(stmt,data)
    results = cxn.fetchall()
    for row in results:
      q1 = row['q1']
      q2 = row['q2']
      q3 = row['q3']
      q4 = row['q4']
      q5 = row['q5']
      q6 = row['q6']
      q7 = row['q7']
      q8 = row['q8']
      q9 = row['q9']
      q10 = row['q10']
      percent = row['correct']
    subs = {
    'percent':percent,
    'a1':q1,
    'a2':q2,
    'a3':q3,
    'a4':q4,
    'a5':q5,
    'a6':q6,
    'a7':q7,
    'a8':q8,
    'a9':q9,
    'a10':q10,
    } 
    html_output = template.substitute(subs)
    print(html_output)

if nameInsert == None:
  cxn.execute(stmt3,data3)
  z = 1
  #print("FOR DEBUG TRACE: Test Flag")
  a = open(r"results.txt")
  template = Template(a.read())
  cxn.execute(stmt,data)
  results = cxn.fetchall()
  for row in results:
    q1 = row['q1']
    q2 = row['q2']
    q3 = row['q3']
    q4 = row['q4']
    q5 = row['q5']
    q6 = row['q6']
    q7 = row['q7']
    q8 = row['q8']
    q9 = row['q9']
    q10 = row['q10']
    #percent = row['correct']
  subs = {
  'percent':x,
  'a1':q1,
  'a2':q2,
  'a3':q3,
  'a4':q4,
  'a5':q5,
  'a6':q6,
  'a7':q7,
  'a8':q8,
  'a9':q9,
  'a10':q10,
  } 
  html_output = template.substitute(subs)
  print(html_output)

if count == 0 and z == 0:
  #print("FOR DEBUG TRACE: Inserted ", nameInsert, " into the database")
  cxn.execute(stmt2,data2)
  a = open(r"quiz.txt")
  template = Template(a.read())
  subs = {'quiz':"Quiz"}
  html_output = template.substitute(subs)
  print(html_output)

#if nameInsert == None and mailInsert == None and e == 0: 
#  a = open(r"web_quiz_template_1.txt")
#  template = Template(a.read())
#  subs = {'title':'Database Design'}
#  html_output = template.substitute(subs)
#  print(html_output)
