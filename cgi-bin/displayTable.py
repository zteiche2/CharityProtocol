#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

c.execute('SELECT * FROM users ')
infoFormat = '%-6s%-15s%-12s%-10s%-10s%-8s'
print infoFormat % ('name', 'email', 'password', 'dateMonth', 'dateDay', 'time')
print '-' * 54
for row in c:
    print infoFormat % row


c.execute('SELECT * FROM surveyData ')
dataFormat = '%-6s%-6s%-6s%-6s%-6s%-6s%-8s'
print dataFormat % ('name', 'mj', 'lgbt', 'gun', 'ref', 'abort', 'MAX')
print '-' * 54
for row in c:
    print dataFormat % row



conn.commit()
conn.close()