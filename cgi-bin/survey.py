#!/usr/bin/env python

#Helper Functions
def show(message): #Returns message (used for bug testing)
  print 'Content-Type: text/html'
  print
  print '''<html>
  <head>
    <title>Survey Results</title>
  </head>
  <body> 
    <h1>''' + message + '''</h1>
  </body>
  </html>'''

  return;

def getScore(topic, form): #returns the calculated score for the inputed question topic
	str2num = {"-3":-3, "-2":-2, "-1":-1, "0":0, "1":1, "2":2, "3":3} #hacky way to convert a form.getvalue() to a
  	
	q1 = form.getvalue(topic + "1")
	q2 = form.getvalue(topic + "2")
	q3 = form.getvalue(topic + "3")
	q4 = form.getvalue(topic + "4")
	q5 = form.getvalue(topic + "5")
	q6 = form.getvalue(topic + "6")
	
  	return (str2num[q1] + str2num[q2] + str2num[q3] + str2num[q4] + str2num[q5] + str2num[q6]);
  	
def getMaxTopic(form): #returns topic user feels strongest about
	#Make conversion tables
	index2topic = {0:"mj", 1:"lgbt", 2:"gun", 3:"ref", 4:"abort"}
	
	#Get scores
	mj = getScore("mj", form)
	lgbt = getScore("lgbt", form)
	gun = getScore("gun", form)
	ref = getScore("ref", form)
	abort = getScore("abort", form)
	#Find max score/topic
	scores = [mj, lgbt, gun, ref, abort]
	abScores = [abs(mj), abs(lgbt), abs(gun), abs(ref), abs(abort)]
	maxTopic = index2topic[abScores.index(max(abScores))]

	
	return maxTopic;


#MAIN
import cgitb
import cgi
import sqlite3
cgitb.enable()


form = cgi.FieldStorage()



#Get User Information and Survey Data
name = form['name'].value
email = form['email'].value
password = form['password'].value
dateMonth = form['dateMonth'].value
dateDay = form['dateDay'].value
time = form['time'].value

mj = getScore("mj", form)
lgbt = getScore("lgbt", form)
gun = getScore("gun", form)
ref = getScore("ref", form)
abort = getScore("abort", form)
maxTopic = getMaxTopic(form)


#Create accounts database and users table if they do not exist
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users(name varchar(100) PRIMARY KEY, email varchar(100), password varchar(100), dateMonth INT, dateDay INT, time varchar(100))')
c.execute('CREATE TABLE IF NOT EXISTS surveyData(name varchar(100) PRIMARY KEY, mj INT, lgbt INT, gun INT, ref INT, abort INT, maxTopic varchar(100))')
c.execute('INSERT into users VALUES (?,?,?,?,?,?)', (name, email, password, dateMonth, dateDay, time))
c.execute('INSERT into surveyData VALUES (?,?,?,?,?,?,?)', (name, mj, lgbt, gun, ref, abort, maxTopic))


print 'Content-Type: text/html'
print
print 'Account Created'

# print 'Content-Type: text/html'
# print
# print '''<html>
#   <head>
#     <title>Survey Results</title>
#   </head>
#   <body>''' 
# c.execute('SELECT * FROM users ')
# infoFormat = '%-6s%-15s%-12s%-14s%-8s'
# print infoFormat % ('name', 'email', 'password', 'date', 'time')
# print '<BR>' 
# print '-' * 54
# print '<BR>'
# for row in c:
#     print infoFormat % row
#     print '<BR>'

# print '<BR>'
# print '<BR>'

# c.execute('SELECT * FROM surveyData ')
# dataFormat = '%-6s%-6s%-6s%-6s%-6s%-6s%-8s'
# print dataFormat % ('name', 'mj', 'lgbt', 'gun', 'ref', 'abort', 'MAX')
# print '<BR>'
# print '-' * 54
# print '<BR>'
# for row in c:
#     print dataFormat % row
#     print '<BR>'

# print '''</body>
#   </html>'''




conn.commit()

conn.close()










